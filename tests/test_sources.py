import copy
import gzip
import io
import json
import tempfile
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse

from cpic_tracker.source import ApiClient, read_release
from cpic_tracker.snapshot import build_snapshot, load_snapshot, save_snapshot

FIXTURES = Path(__file__).parent / 'fixtures'


def tables():
    return {p.stem: json.loads(p.read_text()) for p in FIXTURES.glob('*.json')}


class Response(io.BytesIO):
    def __init__(self, rows, content_range):
        super().__init__(json.dumps(rows).encode())
        self.headers = {'Content-Range': content_range}


class ApiTests(unittest.TestCase):
    def test_pages_even_when_server_caps_page_size(self):
        calls = []
        def fetch(request, timeout):
            q = parse_qs(urlparse(request.full_url).query)
            offset = int(q['offset'][0])
            calls.append((q, dict(request.header_items()), timeout))
            return Response([{'id': offset}], f'{offset}-{offset}/3')
        rows, evidence = ApiClient(opener=fetch, page_size=100).fetch_table('guideline')
        self.assertEqual(rows, [{'id': 0}, {'id': 1}, {'id': 2}])
        self.assertEqual(len(evidence), 3)
        self.assertTrue(all(q['order'] == ['id.asc'] for q, _, _ in calls))
        self.assertEqual(calls[0][1]['Prefer'], 'count=exact')
        self.assertEqual(len(evidence[0]['sha256']), 64)

    def test_rejects_missing_count_empty_page_and_changing_total(self):
        for ranges in [['0-0/*'], ['0-0/2', '*/2'], ['0-0/2', '1-1/3']]:
            iterator = iter(ranges)
            def fetch(request, timeout):
                r = next(iterator)
                return Response([] if r.startswith('*') else [{'id': len(r)}], r)
            with self.subTest(ranges=ranges), self.assertRaises(ValueError):
                ApiClient(opener=fetch).fetch_table('guideline')

    def test_http_denial_is_not_retried(self):
        calls = []
        def fetch(request, timeout):
            calls.append(request.full_url)
            raise HTTPError(request.full_url, 403, 'Forbidden', {}, None)
        with self.assertRaises(HTTPError):
            ApiClient(opener=fetch).fetch_table('pair')
        self.assertEqual(len(calls), 1)

    def test_replays_all_fixed_api_tables_without_network(self):
        source = tables()
        def fetch(request, timeout):
            name = urlparse(request.full_url).path.rsplit('/', 1)[-1]
            rows = source[name]
            return Response(rows, f'0-{len(rows)-1}/{len(rows)}')
        data, evidence = ApiClient(opener=fetch).fetch_all()
        self.assertEqual(data, source)
        self.assertEqual(len(evidence), 5)


class ReleaseTests(unittest.TestCase):
    def test_copy_decoding_preserves_literal_text_and_null(self):
        text = ('COPY cpic.guideline (id, name, url, genes, notesonusage) FROM stdin;\n'
                '1\tName\thttps://example.org/g\t{CYP2C19}\tline\\nnext\\t\\\\literal\n\\.\n')
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'release.sql.gz'
            with gzip.open(p, 'wt') as f:
                f.write(text)
            data = read_release(p, require_all=False)
        self.assertEqual(data['guideline'][0]['notesonusage'], 'line\nnext\t\\literal')
        self.assertEqual(data['guideline'][0]['genes'], ['CYP2C19'])
        self.assertEqual(data['guideline'][0]['id'], 1)

    def test_incomplete_dump_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'empty.gz'
            with gzip.open(p, 'wt') as f:
                f.write('-- incomplete\n')
            with self.assertRaises(ValueError):
                read_release(p)


class SnapshotTests(unittest.TestCase):
    def test_roundtrip_and_no_overwrite(self):
        s = build_snapshot(tables(), {'kind': 'fixture', 'url': 'https://api.cpicpgx.org/v1/'})
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'snapshot.json'
            save_snapshot(s, p)
            self.assertEqual(load_snapshot(p), s)
            with self.assertRaises(FileExistsError):
                save_snapshot(s, p)

    def test_invalid_shapes_references_and_duplicate_ids_rejected(self):
        variants = []
        t = tables(); t['pair'] = []; variants.append(t)
        t = tables(); t['recommendation'][0]['phenotypes'] = 'not an object'; variants.append(t)
        t = tables(); t['guideline'][0]['url'] = None; variants.append(t)
        t = tables(); t['recommendation'][0]['guidelineid'] = -1; variants.append(t)
        t = tables(); t['drug'].append(t['drug'][0]); variants.append(t)
        for variant in variants:
            with self.subTest(variant=variants.index(variant)), self.assertRaises(ValueError):
                build_snapshot(variant, {'kind': 'fixture'})

    def test_tampered_snapshot_rejected(self):
        s = build_snapshot(tables(), {'kind': 'fixture'})
        s['tables']['recommendation'][0]['drugrecommendation'] = 'tampered'
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'snapshot.json'; p.write_text(json.dumps(s))
            with self.assertRaises(ValueError):
                load_snapshot(p)
