"""
Automation — Medium Exercises
==============================
Topics: file organiser, subprocess, logging, argparse, os.walk.

Run:  python 02-medium.py
"""

from pathlib import Path
import shutil
import subprocess
import logging
import os


# ---------------------------------------------------------------------------
# 1. File organiser
# ---------------------------------------------------------------------------
# Implement organise(source_dir) that:
#   - Scans all files (non-recursive) in source_dir
#   - Moves each file into a subdirectory based on its extension:
#       .pdf, .doc, .docx, .txt  → 'documents'
#       .png, .jpg, .jpeg, .gif  → 'images'
#       .mp4, .avi, .mkv         → 'videos'
#       .py, .js, .ts, .sh       → 'scripts'
#       .csv, .json, .xlsx       → 'data'
#       anything else            → 'misc'
#   - Creates the subdirectory if it doesn't exist
#   - Skips directories
#   - Logs each move as INFO: "Moved file.pdf → documents/"
#   - Returns a dict {category: count} of files moved per category
#
# Test it on a synthetic folder you create in setup below.

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def organise(source_dir: str) -> dict:
    # YOUR CODE HERE
    pass


# Test setup — create dummy files
def setup_test_folder(path='test_organise'):
    p = Path(path)
    p.mkdir(exist_ok=True)
    for name in ['report.pdf', 'photo.jpg', 'data.csv', 'script.py',
                 'video.mp4', 'notes.txt', 'archive.zip', 'config.json']:
        (p / name).write_text(f'dummy content for {name}')
    return str(p)

folder = setup_test_folder()
result = organise(folder)
print('Files moved per category:', result)
shutil.rmtree(folder, ignore_errors=True)


# ---------------------------------------------------------------------------
# 2. subprocess — run system commands
# ---------------------------------------------------------------------------
# a) Run 'python --version' and print the output.
# b) Run 'pip list' and print only lines that contain 'requests' or 'beautifulsoup'.
# c) Implement run_safe(cmd: list[str]) → dict that:
#    - Runs the command with capture_output=True and timeout=10
#    - Returns {'stdout': ..., 'stderr': ..., 'returncode': ..., 'ok': bool}
#    - Never raises — catches TimeoutExpired and other exceptions,
#      returning {'ok': False, 'error': str(exc)}

def run_safe(cmd: list) -> dict:
    # YOUR CODE HERE
    pass

print(run_safe(['python', '--version']))
print(run_safe(['nonexistent_command_xyz']))


# ---------------------------------------------------------------------------
# 3. Walking a directory tree
# ---------------------------------------------------------------------------
# Implement dir_stats(root) that walks the directory tree under root
# and returns:
# {
#   'total_files': int,
#   'total_dirs': int,
#   'total_size_bytes': int,
#   'by_extension': {'.py': 5, '.txt': 3, ...},
#   'largest_file': {'path': str, 'size': int},
# }
# Use os.walk (not pathlib.glob).

def dir_stats(root: str) -> dict:
    # YOUR CODE HERE
    pass

import tempfile, os
# Create a temp tree to test
with tempfile.TemporaryDirectory() as tmp:
    for i in range(3):
        d = Path(tmp) / f'sub{i}'
        d.mkdir()
        for j in range(2):
            f = d / f'file{j}.txt'
            f.write_text('x' * (i * 100 + j * 50))
    (Path(tmp) / 'big.py').write_text('y' * 500)
    stats = dir_stats(tmp)
    print('Dir stats:', stats)


# ---------------------------------------------------------------------------
# 4. Logging to file
# ---------------------------------------------------------------------------
# Configure a logger that writes to BOTH 'automation.log' AND the console.
# Format: '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
# Log 5 messages at different levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# Then read 'automation.log' and print the number of lines written.

# YOUR CODE HERE
