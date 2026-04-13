"""
Automation — Medium Solutions
"""

from pathlib import Path
import shutil
import subprocess
import logging
import os
import tempfile


# ---------------------------------------------------------------------------
# 1. File organiser
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

EXTENSION_MAP = {
    '.pdf': 'documents', '.doc': 'documents', '.docx': 'documents', '.txt': 'documents',
    '.png': 'images',    '.jpg': 'images',    '.jpeg': 'images',    '.gif': 'images',
    '.mp4': 'videos',    '.avi': 'videos',    '.mkv': 'videos',
    '.py':  'scripts',   '.js':  'scripts',   '.ts':  'scripts',    '.sh':  'scripts',
    '.csv': 'data',      '.json':'data',       '.xlsx':'data',
}

def organise(source_dir: str) -> dict:
    src = Path(source_dir)
    counts = {}
    for file in src.iterdir():
        if file.is_dir():
            continue
        category = EXTENSION_MAP.get(file.suffix.lower(), 'misc')
        dest_dir = src / category
        dest_dir.mkdir(exist_ok=True)
        shutil.move(str(file), dest_dir / file.name)
        logger.info('Moved %s → %s/', file.name, category)
        counts[category] = counts.get(category, 0) + 1
    return counts


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
# 2. subprocess
# ---------------------------------------------------------------------------
r = subprocess.run(['python', '--version'], capture_output=True, text=True, check=True)
print(r.stdout or r.stderr)

r = subprocess.run(['pip', 'list'], capture_output=True, text=True)
for line in r.stdout.splitlines():
    if any(k in line.lower() for k in ('requests', 'beautifulsoup')):
        print(line)

def run_safe(cmd: list) -> dict:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return {
            'stdout': r.stdout.strip(),
            'stderr': r.stderr.strip(),
            'returncode': r.returncode,
            'ok': r.returncode == 0,
        }
    except Exception as exc:
        return {'ok': False, 'error': str(exc)}

print(run_safe(['python', '--version']))
print(run_safe(['nonexistent_command_xyz']))


# ---------------------------------------------------------------------------
# 3. Walking a directory tree
# ---------------------------------------------------------------------------
def dir_stats(root: str) -> dict:
    total_files = 0
    total_dirs  = 0
    total_size  = 0
    by_ext      = {}
    largest     = {'path': '', 'size': 0}

    for dirpath, dirnames, filenames in os.walk(root):
        total_dirs += len(dirnames)
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            size  = os.path.getsize(fpath)
            ext   = Path(fname).suffix.lower() or '(no ext)'
            total_files += 1
            total_size  += size
            by_ext[ext] = by_ext.get(ext, 0) + 1
            if size > largest['size']:
                largest = {'path': fpath, 'size': size}

    return {
        'total_files': total_files,
        'total_dirs': total_dirs,
        'total_size_bytes': total_size,
        'by_extension': by_ext,
        'largest_file': largest,
    }

with tempfile.TemporaryDirectory() as tmp:
    for i in range(3):
        d = Path(tmp) / f'sub{i}'
        d.mkdir()
        for j in range(2):
            (d / f'file{j}.txt').write_text('x' * (i * 100 + j * 50))
    (Path(tmp) / 'big.py').write_text('y' * 500)
    print('Dir stats:', dir_stats(tmp))


# ---------------------------------------------------------------------------
# 4. Logging to file
# ---------------------------------------------------------------------------
log_path = 'automation.log'
file_handler   = logging.FileHandler(log_path, mode='w', encoding='utf-8')
stream_handler = logging.StreamHandler()
fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
file_handler.setFormatter(fmt)
stream_handler.setFormatter(fmt)

task_logger = logging.getLogger('task')
task_logger.setLevel(logging.DEBUG)
task_logger.addHandler(file_handler)
task_logger.addHandler(stream_handler)

task_logger.debug('Debug message — detailed diagnostics')
task_logger.info('Info message — normal operation')
task_logger.warning('Warning — something unexpected')
task_logger.error('Error — operation failed')
task_logger.critical('Critical — system failure')

lines = Path(log_path).read_text(encoding='utf-8').splitlines()
print(f'\nLog file has {len(lines)} lines')
Path(log_path).unlink(missing_ok=True)
