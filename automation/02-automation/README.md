# Python Automation

Automating repetitive tasks using the standard library and popular tools.

**Install:** `pip install schedule watchdog`

---

## 1. File System Automation — `pathlib` and `shutil`

```python
from pathlib import Path
import shutil

# Navigate and inspect
p = Path('.')
list(p.iterdir())                     # all entries
list(p.glob('**/*.py'))               # recursive glob
list(p.glob('*.txt'))                 # all .txt in current dir

# Read and write
text = Path('file.txt').read_text(encoding='utf-8')
Path('output.txt').write_text('hello', encoding='utf-8')

# Create / delete
Path('new_dir').mkdir(parents=True, exist_ok=True)
Path('old_file.txt').unlink(missing_ok=True)
shutil.rmtree('old_dir', ignore_errors=True)

# Copy and move
shutil.copy('src.txt', 'dst.txt')           # copy file
shutil.copy2('src.txt', 'dst.txt')          # preserve metadata
shutil.move('src.txt', 'new_location/')
shutil.copytree('src_dir/', 'dst_dir/')

# File info
p = Path('script.py')
p.stat().st_size           # size in bytes
p.stat().st_mtime          # last modified (Unix timestamp)
p.suffix                   # '.py'
p.stem                     # 'script'
p.parent                   # parent directory
p.name                     # 'script.py'
```

## 2. OS Automation — `os` and `subprocess`

```python
import os
import subprocess

# Environment variables
os.environ.get('HOME', '/tmp')
os.getenv('API_KEY')

# Working directory
os.getcwd()
os.chdir('/tmp')

# Run shell commands
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)   # 0 = success

# With shell=True (use carefully — risk of shell injection)
result = subprocess.run('echo $HOME', shell=True, capture_output=True, text=True)

# Check for errors automatically
subprocess.run(['python', '--version'], check=True)  # raises on non-zero exit
```

## 3. Working with CSV and JSON

```python
import csv, json
from pathlib import Path

# CSV read
with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# CSV write
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'score'])
    writer.writeheader()
    writer.writerows([{'name': 'Alice', 'score': 95}])

# JSON read/write
data = json.loads(Path('config.json').read_text())
Path('output.json').write_text(json.dumps(data, indent=2, ensure_ascii=False))
```

## 4. Sending Emails with `smtplib`

```python
import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body, from_addr, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From']    = from_addr
    msg['To']      = to
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_addr, password)
        smtp.send_message(msg)
```

> Use an App Password (Gmail) or a dedicated transactional email service in production.

## 5. Scheduling Tasks — `schedule`

```python
import schedule
import time

def report():
    print('Generating daily report...')

def cleanup():
    print('Cleaning temp files...')

schedule.every().day.at('09:00').do(report)
schedule.every(30).minutes.do(cleanup)
schedule.every().monday.do(lambda: print('Weekly digest'))

while True:
    schedule.run_pending()
    time.sleep(60)   # check every minute
```

## 6. Organising Files Automatically

```python
from pathlib import Path
import shutil

RULES = {
    '.pdf':  'documents',
    '.png':  'images',
    '.jpg':  'images',
    '.mp4':  'videos',
    '.py':   'scripts',
    '.csv':  'data',
}

def organise(folder: str):
    src = Path(folder)
    for file in src.iterdir():
        if file.is_file() and file.suffix in RULES:
            dest = src / RULES[file.suffix]
            dest.mkdir(exist_ok=True)
            shutil.move(str(file), dest / file.name)
            print(f'Moved {file.name} → {RULES[file.suffix]}/')
```

## 7. Watching for File Changes — `watchdog`

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f'New file: {event.src_path}')
    def on_modified(self, event):
        if not event.is_directory:
            print(f'Modified: {event.src_path}')

observer = Observer()
observer.schedule(Handler(), path='.', recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

## 8. Logging Instead of print

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler(),          # also print to console
    ]
)

logger = logging.getLogger(__name__)
logger.info('Task started')
logger.warning('Disk usage above 90%%')
logger.error('Failed to connect: %s', str(exc))
```

---

## Quick Reference

```python
# pathlib
Path('dir').mkdir(parents=True, exist_ok=True)
Path('f.txt').read_text() / .write_text()
list(Path('.').glob('**/*.py'))
p.suffix / p.stem / p.parent / p.name

# shutil
shutil.copy / shutil.move / shutil.copytree / shutil.rmtree

# subprocess
subprocess.run(['cmd', 'arg'], capture_output=True, text=True, check=True)

# schedule
schedule.every().day.at('HH:MM').do(fn)
schedule.every(N).minutes.do(fn)
while True: schedule.run_pending(); time.sleep(1)

# logging
logging.basicConfig(level=logging.INFO, format='...', handlers=[...])
logger = logging.getLogger(__name__)
logger.info / .warning / .error
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | pathlib, shutil, CSV/JSON read-write |
| [02-medium.py](exercises/02-medium.py) | Medium | File organiser, subprocess, logging |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Scheduled backup, directory sync, report generator |

Solutions: [solutions/](solutions/)
