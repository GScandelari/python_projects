"""
Automation — Easy Solutions
"""

from pathlib import Path
import shutil
import csv
import json


# ---------------------------------------------------------------------------
# 1. pathlib basics
# ---------------------------------------------------------------------------
print(Path.cwd())
print(list(Path('.').glob('*.py')))

Path('sandbox').mkdir(exist_ok=True)

p = Path('reports/2024/summary.csv')
print(p.name)     # summary.csv
print(p.suffix)   # .csv
print(p.parent)   # reports/2024


# ---------------------------------------------------------------------------
# 2. Read and write text files
# ---------------------------------------------------------------------------
content = "Hello from Python!\nLine 2\nLine 3"
Path('sandbox/hello.txt').write_text(content, encoding='utf-8')

lines = Path('sandbox/hello.txt').read_text(encoding='utf-8').splitlines()
for i, line in enumerate(lines, 1):
    print(f'{i}: {line}')

with open('sandbox/hello.txt', 'a', encoding='utf-8') as f:
    f.write('\nLine 4')

all_lines = Path('sandbox/hello.txt').read_text(encoding='utf-8').splitlines()
print('Total lines:', len(all_lines))


# ---------------------------------------------------------------------------
# 3. Copy and move files
# ---------------------------------------------------------------------------
shutil.copy('sandbox/hello.txt', 'sandbox/hello_backup.txt')
Path('sandbox/archive').mkdir(exist_ok=True)
shutil.move('sandbox/hello_backup.txt', 'sandbox/archive/hello_backup.txt')

for f in Path('sandbox').rglob('*'):
    print(f)


# ---------------------------------------------------------------------------
# 4. CSV read and write
# ---------------------------------------------------------------------------
STUDENTS = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob',   'age': 22, 'grade': 'B'},
    {'name': 'Carol', 'age': 21, 'grade': 'A'},
    {'name': 'David', 'age': 23, 'grade': 'C'},
]

with open('sandbox/students.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'grade'])
    writer.writeheader()
    writer.writerows(STUDENTS)

with open('sandbox/students.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

a_students = [r for r in rows if r['grade'] == 'A']
print('Grade A:', [r['name'] for r in a_students])

avg_age = sum(int(r['age']) for r in rows) / len(rows)
print(f'Average age: {avg_age:.1f}')


# ---------------------------------------------------------------------------
# 5. JSON read and write
# ---------------------------------------------------------------------------
CONFIG = {
    'app': 'MyApp', 'version': '2.1.0', 'debug': False,
    'database': {'host': 'localhost', 'port': 5432},
    'allowed_hosts': ['127.0.0.1', 'localhost'],
}

Path('sandbox/config.json').write_text(
    json.dumps(CONFIG, indent=2), encoding='utf-8'
)

data = json.loads(Path('sandbox/config.json').read_text(encoding='utf-8'))
print(data['database']['host'], data['database']['port'])

data['version'] = '2.2.0'
Path('sandbox/config.json').write_text(
    json.dumps(data, indent=2), encoding='utf-8'
)

verify = json.loads(Path('sandbox/config.json').read_text(encoding='utf-8'))
print('Version:', verify['version'])


# ---------------------------------------------------------------------------
# 6. Cleanup
# ---------------------------------------------------------------------------
shutil.rmtree('sandbox', ignore_errors=True)
print('Cleaned up sandbox/')
