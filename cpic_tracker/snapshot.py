"""Versioned, validated, write-once snapshot files."""
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

from .source import COLUMNS, ORDER, JSON_FIELDS, utc_now


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


def validate_tables(tables):
    if not isinstance(tables, dict) or set(tables) != set(COLUMNS):
        raise ValueError('snapshot must contain all five source tables')
    indexes = {}
    for name, columns in COLUMNS.items():
        rows = tables[name]
        if not isinstance(rows, list) or not rows:
            raise ValueError('empty or invalid table: ' + name)
        index = {}
        for row in rows:
            if not isinstance(row, dict) or not set(columns.split()).issubset(row):
                raise ValueError('missing source columns: ' + name)
            key = row[ORDER[name]]
            if key is None or key in index:
                raise ValueError('duplicate or null source id: ' + name)
            index[key] = row
            for field in JSON_FIELDS.intersection(row):
                if not isinstance(row[field], dict):
                    raise ValueError('invalid JSON object: ' + field)
        indexes[name] = index
    for row in tables['guideline']:
        url = urlparse(row['url'] or '')
        if url.scheme not in {'https', 'http'} or not url.netloc:
            raise ValueError('guideline missing source URL')
    for name in ('pair', 'recommendation', 'publication', 'drug'):
        for row in tables[name]:
            gid = row['guidelineid']
            if gid is not None and gid not in indexes['guideline']:
                raise ValueError('unknown guideline reference in ' + name)
            if name in ('pair', 'recommendation') and row['drugid'] not in indexes['drug']:
                raise ValueError('unknown drug reference in ' + name)
    return tables


def build_snapshot(tables, source, started_at=None):
    validate_tables(tables)
    now = utc_now()
    return {'schema_version': 1, 'started_at': started_at or now, 'captured_at': now,
            'source': source, 'tables_sha256': digest(tables), 'tables': tables}


def load_snapshot(path):
    snapshot = json.loads(Path(path).read_text(encoding='utf-8'))
    if snapshot.get('schema_version') != 1:
        raise ValueError('unsupported snapshot schema')
    validate_tables(snapshot['tables'])
    if digest(snapshot['tables']) != snapshot.get('tables_sha256'):
        raise ValueError('snapshot checksum mismatch')
    return snapshot


def save_snapshot(snapshot, path):
    validate_tables(snapshot['tables'])
    if digest(snapshot['tables']) != snapshot['tables_sha256']:
        raise ValueError('snapshot checksum mismatch')
    # Exclusive creation protects dated evidence from accidental overwrite.
    with Path(path).open('x', encoding='utf-8') as stream:
        json.dump(snapshot, stream, indent=2, ensure_ascii=False, sort_keys=True)
        stream.write('\n')
