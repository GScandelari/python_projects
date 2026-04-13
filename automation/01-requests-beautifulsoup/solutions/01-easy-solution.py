"""
Requests & BeautifulSoup — Easy Solutions
"""

import requests


# ---------------------------------------------------------------------------
# 1. Basic GET request
# ---------------------------------------------------------------------------
r = requests.get('https://httpbin.org/get', timeout=10)
print(r.status_code)          # 200
print(r.json()['url'])        # https://httpbin.org/get
print(r.ok)                   # True


# ---------------------------------------------------------------------------
# 2. Query parameters
# ---------------------------------------------------------------------------
r = requests.get('https://httpbin.org/get',
                 params={'name': 'Alice', 'language': 'Python', 'level': 3},
                 timeout=10)
print(r.json()['args'])       # {'language': 'Python', 'level': '3', 'name': 'Alice'}
print(r.url)                  # URL with ?name=Alice&language=Python&level=3


# ---------------------------------------------------------------------------
# 3. Response headers
# ---------------------------------------------------------------------------
r = requests.get('https://httpbin.org/response-headers',
                 params={'X-Custom-Header': 'hello', 'Content-Type': 'application/json'},
                 timeout=10)
for key, value in r.headers.items():
    print(f'{key}: {value}')


# ---------------------------------------------------------------------------
# 4. Status codes
# ---------------------------------------------------------------------------
for code in [200, 201, 301, 400, 404, 500]:
    try:
        r = requests.get(f'https://httpbin.org/status/{code}',
                         timeout=10, allow_redirects=False)
        label = 'OK' if r.ok else 'NOT OK'
        print(f'{r.status_code}: {label} (ok={r.ok})')
    except Exception as e:
        print(f'{code}: ERROR — {e}')


# ---------------------------------------------------------------------------
# 5. PokeAPI
# ---------------------------------------------------------------------------
r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto', timeout=10)
r.raise_for_status()
data = r.json()
print(data['name'])                                       # ditto
print(data['base_experience'])                            # 101
for ability in data['abilities'][:3]:
    print(ability['ability']['name'])                     # limber, imposter, ...


# ---------------------------------------------------------------------------
# 6. Download image
# ---------------------------------------------------------------------------
r = requests.get('https://httpbin.org/image/png', timeout=10)
print(r.headers['Content-Type'])    # image/png
print(len(r.content), 'bytes')
with open('downloaded.png', 'wb') as f:
    f.write(r.content)
print('Saved to downloaded.png')
