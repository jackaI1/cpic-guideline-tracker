# CPIC guideline tracker

I built a guideline change tracker because I wanted a way to see what changed without comparing drug recommendation tables by hand. CPIC, the Clinical Pharmacogenetics Implementation Consortium, publishes guidance about how genetic differences can affect drug prescribing. I save dated copies of its public data, compare them, and link each change back to its source.

I can also look up a drug and a gene phenotype, a description such as “Poor Metabolizer.” The tool returns CPIC's recommendation text verbatim with its guideline link and publication citations. If the saved data has no exact supported match, it says **“no guideline”** instead of guessing.

**This is a learning project, not clinical decision support. Do not use it to choose a drug or dose.** A lookup is limited to the saved snapshot and supported inputs. Read the full source guideline, including its limitations.

## Read it without installing anything

- [Saved change report](reports/release-changes.md): an actual comparison of CPIC releases, with before-and-after values and source links.
- [Saved lookup result](reports/lookup-example.json): the original recommendation text, comments, population and citations for an example query.
- [Live API snapshot](snapshots/api-2026-11-05.json): the downloaded source rows, retrieval times and page checksums.

I keep gene-drug pairs and CPIC levels, the evidence categories assigned by CPIC, separately from recommendations. A pair being listed does not mean that CPIC has a recommendation for it. Some pairs have no linked guideline; their report entries say so and link to the CPIC source record instead of inventing a guideline link.

## Try it

From a local copy of this repository, run these commands with Python. There are no packages to install. These examples use the saved files and do not need the internet.

```sh
python3 -m cpic_tracker lookup snapshots/release-v1.61.0.json \
  --drug voriconazole --phenotype 'CYP2C19=Poor Metabolizer' --population adults

python3 -m cpic_tracker lookup snapshots/release-v1.61.0.json \
  --drug unknown-drug --phenotype 'CYP2C19=Poor Metabolizer'

python3 -m cpic_tracker compare \
  snapshots/release-v1.57.0.json snapshots/release-v1.61.0.json
```

The first query returns the exact source wording and its context. The second returns “no guideline.” Drug names, gene names and phenotype values ignore capitalization and surrounding spaces; there is no fuzzy matching or conversion from a genotype, the underlying genetic result.

If several populations match, the tool asks for a population without returning a recommendation. Repeat `--phenotype 'GENE=VALUE'` for a guideline that explicitly uses several phenotypes. All required genes must match. I deliberately reject rows that require allele status or an activity score, a numerical measure of gene function, rather than infer those from a phenotype. “No guideline” means no supported exact match **in this snapshot**, not proof that no guidance exists anywhere.

## Save a fresh snapshot

This command calls the public CPIC API, an interface for downloading structured data, and writes a new file named with the current UTC time:

```sh
python3 -m cpic_tracker snapshot
```

To choose a filename, use `snapshot --output my-new-snapshot.json`. Existing files are never overwritten. Compare any saved pair with `compare old.json new.json --output my-report.md`; add `--json` for structured changes.

The live capture in this repository was downloaded successfully from the data endpoints. An initial request for the API documentation returned HTTP 403, so I also added an importer for CPIC's official public database exports. The historical comparison uses those releases, not invented earlier API captures. Both release files were retrieved when I built the report; their release labels are not retrieval dates. [Reproduction instructions](docs/data-and-design.md) include download commands and source checksums.

## How I organized it

I use Python's standard library to download data and store JSON, a readable text format. Each snapshot includes the source, retrieval window and a checksum that detects changed saved rows. The API reader follows every page in a stable order and checks exact row counts so a shortened download fails instead of appearing as deleted guidelines.

I compare recommendations by drug, guideline, population and the complete source lookup key, the set of gene conditions attached to a recommendation. I ignore regenerated recommendation row IDs. The report tracks recommendation text, comments, implications, classification, pair levels, retirement, guideline details, drug names and publication citations. It describes data changes, not their medical significance.

The API does not promise a single database transaction across requests. Matching page counts cannot detect every edit made during a download. For reproducible historical comparisons I use the published release exports. I parse their text as data and never execute their SQL, the database instruction language. More detail is in [data and design](docs/data-and-design.md).

## Public sources

- [CPIC public API and endpoint reference](https://api.cpicpgx.org/), specifically `pair`, `drug`, `guideline`, `recommendation` and guideline-linked `publication` rows.
- [CPIC data model documentation](https://github.com/cpicpgx/cpic-data/wiki), including phenotype, activity-score, allele-status and population distinctions.
- Official database exports linked from [the earlier release](https://github.com/cpicpgx/cpic-data/releases/tag/v1.57.0) and [the later release](https://github.com/cpicpgx/cpic-data/releases/tag/v1.61.0). The snapshot manifests record each exact download URL and checksum.
- [CPIC resources](https://www.clinpgx.org/page/cpicResources) and [data use and citation policy](https://www.clinpgx.org/page/dataUsagePolicy). Source data retains its original terms; this project does not claim authorship of CPIC recommendations.

Each lookup includes the guideline URL and the publications associated with that guideline. That list is guideline-level bibliography, not a claim that every paper independently supports that particular row. I use only public reference data and no patient records.

## Checks and measured results

The checked-in live snapshot contains **635 pair rows**, **570 active pairs**, **2,159 recommendation rows**, and **29 guidelines**. Reproduce these figures with:

```sh
python3 -m cpic_tracker stats snapshots/api-2026-11-05.json
```

The saved historical report contains **54 changed records**. Generate the same report with the `compare` command above; the detailed entries show which fields changed.

```sh
python3 -m unittest discover -v
```

GitHub Actions runs the tests on the supported Python versions and regenerates the saved report and lookup example. Tests use fixed subsets of the real API response plus explicitly labelled synthetic mutations for error and change cases. They cover pagination, interrupted downloads, snapshot integrity, source links, exact text, missing guidance, retirement, population selection and incomplete inputs. No test needs the network.
