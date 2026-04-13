# Requests & BeautifulSoup

Making HTTP requests and parsing HTML to extract data from the web.

**Install:** `pip install requests beautifulsoup4 lxml`

---

## 1. HTTP Requests with `requests`

```python
import requests

# GET
response = requests.get('https://httpbin.org/get')
print(response.status_code)   # 200
print(response.json())        # parsed JSON body

# With query params
response = requests.get('https://httpbin.org/get', params={'q': 'python', 'page': 1})
# builds: https://httpbin.org/get?q=python&page=1

# With headers
headers = {'User-Agent': 'MyBot/1.0', 'Accept': 'application/json'}
response = requests.get('https://httpbin.org/headers', headers=headers)

# POST with JSON body
response = requests.post('https://httpbin.org/post',
                         json={'name': 'Alice', 'score': 99})

# Timeouts — always set them!
response = requests.get('https://httpbin.org/delay/1', timeout=5)
```

## 2. Response Object

```python
r = requests.get('https://httpbin.org/get')

r.status_code      # 200
r.ok               # True if 200–299
r.headers          # dict-like response headers
r.text             # body as string
r.content          # body as bytes
r.json()           # body parsed as JSON (raises if not JSON)
r.url              # final URL after redirects
r.elapsed          # timedelta — how long the request took

# Raise an exception for 4xx/5xx
r.raise_for_status()   # raises requests.HTTPError
```

## 3. Sessions

A `Session` reuses the TCP connection and persists cookies and headers across requests.

```python
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer my-token'})

    r1 = session.get('https://api.example.com/profile')
    r2 = session.get('https://api.example.com/posts')
    # same connection and headers for both
```

## 4. Error Handling

```python
from requests.exceptions import HTTPError, Timeout, ConnectionError

try:
    r = requests.get('https://httpbin.org/status/404', timeout=5)
    r.raise_for_status()
except HTTPError as e:
    print(f'HTTP error: {e.response.status_code}')
except Timeout:
    print('Request timed out')
except ConnectionError:
    print('Network unavailable')
```

## 5. Parsing HTML with BeautifulSoup

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1 class="title">Hello</h1>
    <ul id="list">
      <li><a href="/a">Link A</a></li>
      <li><a href="/b">Link B</a></li>
    </ul>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')   # or 'html.parser'

# Finding elements
soup.find('h1')                      # first <h1>
soup.find('h1', class_='title')      # with CSS class
soup.find_all('a')                   # all <a> tags
soup.find_all('li', limit=5)         # first 5

# CSS selectors (most flexible)
soup.select('ul#list a')             # <a> inside ul#list
soup.select_one('h1.title')          # first match

# Extracting data
tag = soup.find('h1')
tag.text                             # 'Hello'
tag.get_text(strip=True)             # 'Hello' (stripped)
tag['class']                         # ['title']
tag.get('href', '')                  # safe attribute access
```

## 6. Navigating the Tree

```python
soup.body.h1                         # direct child access
tag.parent                           # parent element
tag.next_sibling                     # next sibling
list(tag.children)                   # direct children
list(tag.descendants)                # all descendants

# Find by text content
soup.find(string='Hello')
soup.find_all(string=lambda t: 'python' in t.lower())
```

## 7. Scraping Pattern

```python
import requests
from bs4 import BeautifulSoup
import time

BASE_URL = 'https://books.toscrape.com'

def scrape_page(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')

    books = []
    for article in soup.select('article.product_pod'):
        books.append({
            'title': article.h3.a['title'],
            'price': article.select_one('.price_color').text,
            'rating': article.p['class'][1],
        })
    return books

# Polite crawling: respect the server
books = scrape_page(f'{BASE_URL}/catalogue/page-1.html')
time.sleep(1)   # delay between requests
```

## 8. Consuming REST APIs

```python
import requests

# Public API — no auth required
r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu', timeout=10)
r.raise_for_status()
data = r.json()
print(data['name'], data['base_experience'])

# Paginated API
def fetch_all_pages(base_url):
    results = []
    url = base_url
    while url:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        page = r.json()
        results.extend(page['results'])
        url = page.get('next')   # None when last page
    return results
```

---

## Quick Reference

```python
import requests
from bs4 import BeautifulSoup

# Request
r = requests.get(url, params={}, headers={}, timeout=10)
r = requests.post(url, json={}, timeout=10)
r.raise_for_status()
data = r.json()

# Session (connection reuse, shared headers/cookies)
with requests.Session() as s:
    s.headers.update({...})
    s.get(url)

# Parse HTML
soup = BeautifulSoup(r.text, 'lxml')
soup.find('tag', class_='name')
soup.find_all('tag')
soup.select('css selector')
soup.select_one('css selector')
tag.text / tag.get_text(strip=True)
tag['attr'] / tag.get('attr', default)
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | GET requests, status codes, JSON APIs |
| [02-medium.py](exercises/02-medium.py) | Medium | Session, error handling, HTML parsing |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Multi-page scraper, pagination, CSV export |

Solutions: [solutions/](solutions/)
