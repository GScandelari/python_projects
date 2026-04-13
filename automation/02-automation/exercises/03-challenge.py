"""
Automation — Challenge Exercises
==================================
Topics: scheduled backup, directory sync, report generator,
        config-driven automation, file watcher.

Run:  python 03-challenge.py
"""

from pathlib import Path
import shutil
import json
import csv
import logging
import hashlib
import datetime


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 1. Timestamped backup utility
# ---------------------------------------------------------------------------
# Implement backup(source_dir, backup_root) that:
#   - Creates a timestamped folder inside backup_root:
#       backup_root/YYYY-MM-DD_HH-MM-SS/
#   - Copies the entire source_dir tree into it (shutil.copytree)
#   - Writes a manifest.json inside the backup folder with:
#       {'source': str, 'timestamp': str, 'files': int, 'size_bytes': int}
#   - Returns the path to the backup folder
#   - Logs the result

def backup(source_dir: str, backup_root: str) -> Path:
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# 2. Directory sync (one-way)
# ---------------------------------------------------------------------------
# Implement sync(source, target) that mirrors source into target:
#   - Copies files that exist in source but not in target
#   - Updates files that exist in both but differ (compare by MD5 hash)
#   - Deletes files from target that no longer exist in source
#   - Skips directories — only sync files (keep target subdirs in sync too)
#   - Returns {'copied': n, 'updated': n, 'deleted': n}
#
# Hint: compute MD5 with hashlib.md5(file.read_bytes()).hexdigest()

def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()

def sync(source: str, target: str) -> dict:
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# 3. Report generator
# ---------------------------------------------------------------------------
# Implement generate_report(data_dir, output_file) that:
#   - Reads all *.csv files from data_dir
#   - Each CSV has columns: date, product, units, price
#   - Computes:
#       total_revenue (sum of units * price across all files)
#       total_units
#       revenue_by_product {product: revenue}
#       top_product (highest revenue)
#   - Writes a JSON report to output_file
#   - Returns the report dict

def generate_report(data_dir: str, output_file: str) -> dict:
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# 4. Config-driven file processor
# ---------------------------------------------------------------------------
# Implement process(config_path) that reads a JSON config file like:
# {
#   "source_dir": "input/",
#   "output_dir": "output/",
#   "rules": [
#     {"match": "*.log",  "action": "delete"},
#     {"match": "*.txt",  "action": "copy"},
#     {"match": "*.csv",  "action": "move"}
#   ]
# }
#
# For each file in source_dir:
#   - Check each rule in order (fnmatch against the filename)
#   - Apply the first matching rule:
#       "delete" → delete the file
#       "copy"   → copy to output_dir
#       "move"   → move to output_dir
#   - Log every action
#   - Return {'deleted': n, 'copied': n, 'moved': n, 'skipped': n}

import fnmatch

def process(config_path: str) -> dict:
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# Test harness
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    import tempfile, os

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # --- Test 1: backup ---
        src = tmp / 'source'
        src.mkdir()
        (src / 'a.txt').write_text('hello')
        (src / 'b.py').write_text('print("hi")')
        bk_root = tmp / 'backups'
        bk_root.mkdir()
        bk_path = backup(str(src), str(bk_root))
        if bk_path:
            print('Backup created at:', bk_path)
            print('Manifest:', (bk_path / 'manifest.json').read_text())

        # --- Test 2: sync ---
        target = tmp / 'target'
        target.mkdir()
        (target / 'old.txt').write_text('stale')
        sync(str(src), str(target))
        print('Target contents:', [f.name for f in target.iterdir()])

        # --- Test 3: report ---
        data_dir = tmp / 'data'
        data_dir.mkdir()
        for i, (product, units, price) in enumerate([
                ('Widget', 10, 9.99), ('Gadget', 5, 24.99), ('Widget', 8, 9.99)]):
            (data_dir / f'sales_{i}.csv').write_text(
                'date,product,units,price\n'
                f'2024-01-0{i+1},{product},{units},{price}\n'
            )
        report = generate_report(str(data_dir), str(tmp / 'report.json'))
        if report:
            print('Report:', json.dumps(report, indent=2))
