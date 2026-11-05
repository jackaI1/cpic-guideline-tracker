# CPIC snapshot change report

Learning project, not clinical decision support. These are source-data changes, not interpretations of medical significance.

Before: v1.57.0; retrieved 2026-11-05T06:15:43.313197+00:00
After: v1.61.0; retrieved 2026-11-05T06:15:43.631694+00:00

Total changed records: 54

| Table | Added | Removed | Changed |
| --- | ---: | ---: | ---: |
| pair | 1 | 0 | 7 |
| recommendation | 0 | 0 | 42 |
| guideline | 0 | 0 | 0 |
| drug | 1 | 0 | 2 |
| publication | 1 | 0 | 0 |

Recommendation keys include drug, guideline, population and the full gene lookup key. A key change appears as a removal and an addition. Regenerated recommendation IDs are ignored.

Pairs without a CPIC-linked guideline link to their source record and are labelled explicitly.

## Added: pair \['CYP2D6', 'Drugbank:DB09290'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: cpiclevel, drugid, genesymbol, guidelineid, removed, usedforrecommendation

Before:

```json
null
```

After:

```json
{
  "cpiclevel": "C",
  "drugid": "Drugbank:DB09290",
  "genesymbol": "CYP2D6",
  "guidelineid": 100417,
  "removed": false,
  "usedforrecommendation": false
}
```

## Changed: pair \['CYP2D6', 'RxNorm:68091'\]

[No linked guideline; current CPIC API source record](https://api.cpicpgx.org/v1/pair?pairid=eq.110328)
[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: guidelineid

Before:

```json
{
  "guidelineid": null
}
```

After:

```json
{
  "guidelineid": 100417
}
```

## Changed: pair \['CYP2D6', 'RxNorm:70561'\]

[No linked guideline; current CPIC API source record](https://api.cpicpgx.org/v1/pair?pairid=eq.110379)
[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: guidelineid

Before:

```json
{
  "guidelineid": null
}
```

After:

```json
{
  "guidelineid": 100417
}
```

## Changed: pair \['IFNL3', 'RxNorm:120608'\]

[Source guideline: IFNL3 and Peginterferon-alpha-based Regimens](https://www.clinpgx.org/guideline/PA166251455)

Fields: cpiclevel

Before:

```json
{
  "cpiclevel": "A"
}
```

After:

```json
{
  "cpiclevel": "Retired"
}
```

## Changed: pair \['IFNL3', 'RxNorm:253453'\]

[Source guideline: IFNL3 and Peginterferon-alpha-based Regimens](https://www.clinpgx.org/guideline/PA166251455)

Fields: cpiclevel

Before:

```json
{
  "cpiclevel": "A"
}
```

After:

```json
{
  "cpiclevel": "Retired"
}
```

## Changed: pair \['IFNL3', 'RxNorm:9344'\]

[Source guideline: IFNL3 and Peginterferon-alpha-based Regimens](https://www.clinpgx.org/guideline/PA166251455)

Fields: cpiclevel

Before:

```json
{
  "cpiclevel": "A"
}
```

After:

```json
{
  "cpiclevel": "Retired"
}
```

## Changed: pair \['IFNL4', 'RxNorm:120608'\]

[Source guideline: IFNL3 and Peginterferon-alpha-based Regimens](https://www.clinpgx.org/guideline/PA166251455)

Fields: cpiclevel

Before:

```json
{
  "cpiclevel": "A"
}
```

After:

```json
{
  "cpiclevel": "Retired"
}
```

## Changed: pair \['IFNL4', 'RxNorm:253453'\]

[Source guideline: IFNL3 and Peginterferon-alpha-based Regimens](https://www.clinpgx.org/guideline/PA166251455)

Fields: cpiclevel

Before:

```json
{
  "cpiclevel": "A"
}
```

After:

```json
{
  "cpiclevel": "Retired"
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "0.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 poor metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "0.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "0.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "0.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "1.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "1.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "1.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "1.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "2.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "2.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "2.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "2.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "3.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "4.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥3.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥3.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥3.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥3.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥4.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥5.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:26225', 'general', '{"CYP2D6": "≥6.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "0.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 poor metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "0.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "0.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "0.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "1.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugrecommendation, implications

Before:

```json
{
  "drugrecommendation": "Insufficient evidence demonstrating clinical impact based on CYP2D6 genotype. Initiate therapy with recommended starting dose.",
  "implications": {
    "CYP2D6": "Very limited data available for CYP2D6 intermediate metabolizers"
  }
}
```

After:

```json
{
  "drugrecommendation": "No recommendation based on insufficient evidence",
  "implications": {
    "CYP2D6": "Insufficient evidence demonstrating clinical impact"
  }
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "1.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "1.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "1.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "2.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "2.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "2.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "2.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "3.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "4.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥3.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥3.25"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥3.5"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥3.75"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥4.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥5.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Changed: recommendation \[100417, 'RxNorm:27392', 'general', '{"CYP2D6": "≥6.0"}'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: comments

Before:

```json
{
  "comments": "Drug-drug interactions and other patient characteristics (e.g., age, renal function, and liver function) should be considered when selecting alternative therapy. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

After:

```json
{
  "comments": "Drug-drug interactions, the involvement of other metabolizing enzymes and other patient characteristics (e.g., age, renal and hepatic function) should be considered when selecting alternative therapy, as emerging evidence may further clarify the role of enzymes beyond CYP2D6 in the metabolism of the drug. Dolasetron, palonosetron, and ramosetron are also metabolized by CYP2D6. Limited evidence is available regarding the utilization of CYP2D6 genetic variation to guide use of these drugs."
}
```

## Added: drug \['Drugbank:DB09290'\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: drugid, guidelineid, name

Before:

```json
null
```

After:

```json
{
  "drugid": "Drugbank:DB09290",
  "guidelineid": 100417,
  "name": "ramosetron"
}
```

## Changed: drug \['RxNorm:68091'\]

[No linked guideline; current CPIC API source record](https://api.cpicpgx.org/v1/drug?drugid=eq.RxNorm%3A68091)
[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: guidelineid

Before:

```json
{
  "guidelineid": null
}
```

After:

```json
{
  "guidelineid": 100417
}
```

## Changed: drug \['RxNorm:70561'\]

[No linked guideline; current CPIC API source record](https://api.cpicpgx.org/v1/drug?drugid=eq.RxNorm%3A70561)
[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: guidelineid

Before:

```json
{
  "guidelineid": null
}
```

After:

```json
{
  "guidelineid": 100417
}
```

## Added: publication \[8099732\]

[Source guideline: CYP2D6 and Ondansetron and Tropisetron](https://www.clinpgx.org/guideline/PA166251457)

Fields: authors, doi, guidelineid, id, pmid, title, year

Before:

```json
null
```

After:

```json
{
  "authors": [
    "Moore Claire",
    "Bourque Melissa S",
    "Halman Andreas",
    "Agúndez José A G",
    "Prows Cynthia A",
    "Hikino Keiko",
    "Schwab Matthias",
    "Oxencis Carolyn J",
    "Chauhan Dharmisha",
    "Diekstra Meta H M",
    "Long Susie E",
    "Bell Gillian C",
    "Gaedigk Andrea",
    "Whirl-Carrillo Michelle",
    "Klein Teri E",
    "Caudle Kelly E",
    "Conyers Rachel"
  ],
  "doi": "10.1002/cpt.70291",
  "guidelineid": 100417,
  "id": 8099732,
  "pmid": "41979467",
  "title": "Clinical Pharmacogenetics Implementation Consortium (CPIC) Guideline for CYP2D6 Genotype and Use of 5-HT 3 Receptor Antagonists: 2026 Update.",
  "url": null,
  "year": 2026
}
```
