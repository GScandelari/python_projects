"""
Automation — Challenge Solutions
"""

from pathlib import Path
import shutil
import json
import csv
import logging
import hashlib
import datetime
import fnmatch
import tempfile
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 1. Timestamped backup
# ---------------------------------------------------------------------------
def backup(source_dir: str, backup_root: str) -> Path:
    src  = Path(source_dir)
    root = Path(backup_root)
    ts   = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    dest = root / ts
    shutil.copytree(str(src), str(dest))

    files = list(dest.rglob('*'))
    file_list = [f for f in files if f.is_file() and f.name != 'manifest.json']
    size = sum(f.stat().st_size for f in file_list)

    manifest = {
        'source':    str(src.resolve()),
        'timestamp': ts,
        'files':     len(file_list),
        'size_bytes': size,
    }
    (dest / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    logger.info('Backup created at %s (%d files, %d bytes)', dest, len(file_list), size)
    return dest


# ---------------------------------------------------------------------------
# 2. Directory sync (one-way)
# ---------------------------------------------------------------------------
def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()

def sync(source: str, target: str) -> dict:
    src = Path(source)
    tgt = Path(target)
    tgt.mkdir(parents=True, exist_ok=True)
    counts = {'copied': 0, 'updated': 0, 'deleted': 0}

    src_files = {f.relative_to(src): f for f in src.rglob('*') if f.is_file()}
    tgt_files = {f.relative_to(tgt): f for f in tgt.rglob('*') if f.is_file()}

    for rel, src_file in src_files.items():
        tgt_file = tgt / rel
        tgt_file.parent.mkdir(parents=True, exist_ok=True)
        if rel not in tgt_files:
            shutil.copy2(str(src_file), str(tgt_file))
            logger.info('Copied %s', rel)
            counts['copied'] += 1
        elif file_hash(src_file) != file_hash(tgt_file):
            shutil.copy2(str(src_file), str(tgt_file))
            logger.info('Updated %s', rel)
            counts['updated'] += 1

    for rel in tgt_files:
        if rel not in src_files:
            (tgt / rel).unlink()
            logger.info('Deleted %s', rel)
            counts['deleted'] += 1

    return counts


# ---------------------------------------------------------------------------
# 3. Report generator
# ---------------------------------------------------------------------------
def generate_report(data_dir: str, output_file: str) -> dict:
    total_revenue = 0.0
    total_units   = 0
    by_product    = {}

    for csv_file in Path(data_dir).glob('*.csv'):
        with open(csv_file, newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                units   = int(row['units'])
                price   = float(row['price'])
                product = row['product']
                rev     = units * price
                total_revenue += rev
                total_units   += units
                by_product[product] = by_product.get(product, 0) + rev

    top = max(by_product, key=by_product.get) if by_product else None
    report = {
        'total_revenue':    round(total_revenue, 2),
        'total_units':      total_units,
        'revenue_by_product': {k: round(v, 2) for k, v in by_product.items()},
        'top_product':      top,
    }
    Path(output_file).write_text(json.dumps(report, indent=2))
    logger.info('Report written to %s', output_file)
    return report


# ---------------------------------------------------------------------------
# 4. Config-driven file processor
# ---------------------------------------------------------------------------
def process(config_path: str) -> dict:
    cfg = json.loads(Path(config_path).read_text())
    src    = Path(cfg['source_dir'])
    out    = Path(cfg['output_dir'])
    rules  = cfg['rules']
    counts = {'deleted': 0, 'copied': 0, 'moved': 0, 'skipped': 0}

    out.mkdir(parents=True, exist_ok=True)

    for file in src.iterdir():
        if not file.is_file():
            continue
        matched = False
        for rule in rules:
            if fnmatch.fnmatch(file.name, rule['match']):
                action = rule['action']
                if action == 'delete':
                    file.unlink()
                    logger.info('Deleted %s', file.name)
                    counts['deleted'] += 1
                elif action == 'copy':
                    shutil.copy2(str(file), out / file.name)
                    logger.info('Copied %s → output/', file.name)
                    counts['copied'] += 1
                elif action == 'move':
                    shutil.move(str(file), out / file.name)
                    logger.info('Moved %s → output/', file.name)
                    counts['moved'] += 1
                matched = True
                break
        if not matched:
            logger.info('Skipped %s (no rule matched)', file.name)
            counts['skipped'] += 1

    return counts


# ---------------------------------------------------------------------------
# Test harness
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # Test 1: backup
        src = tmp / 'source'
        src.mkdir()
        (src / 'a.txt').write_text('hello')
        (src / 'b.py').write_text('print("hi")')
        bk_root = tmp / 'backups'
        bk_root.mkdir()
        bk_path = backup(str(src), str(bk_root))
        print('Backup at:', bk_path)
        print('Manifest:', (bk_path / 'manifest.json').read_text())

        # Test 2: sync
        target = tmp / 'target'
        target.mkdir()
        (target / 'old.txt').write_text('stale')
        result = sync(str(src), str(target))
        print('Sync result:', result)
        print('Target:', [f.name for f in target.iterdir()])

        # Test 3: report
        data_dir = tmp / 'data'
        data_dir.mkdir()
        for i, (product, units, price) in enumerate([
                ('Widget', 10, 9.99), ('Gadget', 5, 24.99), ('Widget', 8, 9.99)]):
            (data_dir / f'sales_{i}.csv').write_text(
                'date,product,units,price\n'
                f'2024-01-0{i+1},{product},{units},{price}\n'
            )
        report = generate_report(str(data_dir), str(tmp / 'report.json'))
        print('Report:', json.dumps(report, indent=2))

        # Test 4: config processor
        input_dir  = tmp / 'input';  input_dir.mkdir()
        output_dir = tmp / 'output'
        for name in ['app.log', 'readme.txt', 'sales.csv', 'photo.png']:
            (input_dir / name).write_text('content')
        cfg = {
            'source_dir': str(input_dir),
            'output_dir': str(output_dir),
            'rules': [
                {'match': '*.log', 'action': 'delete'},
                {'match': '*.txt', 'action': 'copy'},
                {'match': '*.csv', 'action': 'move'},
            ],
        }
        cfg_file = tmp / 'config.json'
        cfg_file.write_text(json.dumps(cfg))
        print('Processor result:', process(str(cfg_file)))
