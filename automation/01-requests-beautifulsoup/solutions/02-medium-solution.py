"""
Requests & BeautifulSoup — Medium Solutions
"""

import requests
from bs4 import BeautifulSoup
import time
from requests.exceptions import HTTPError, Timeout, ConnectionError


# ---------------------------------------------------------------------------
# 1. Session with shared headers
# ---------------------------------------------------------------------------
with requests.Session() as s:
    s.headers.update({'User-Agent': 'PythonScraper/1.0', 'Accept': 'application/json'})
    r1 = s.get('https://httpbin.org/headers', timeout=10)
    r2 = s.get('https://httpbin.org/get', timeout=10)
    print('Headers response:', r1.json()['headers'].get('User-Agent'))
    print('Get response:', r2.json()['headers'].get('User-Agent'))


# ---------------------------------------------------------------------------
# 2. Robust fetcher with retry
# ---------------------------------------------------------------------------
def fetch(url, retries=3, delay=1.0):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r
        except (HTTPError, Timeout, ConnectionError) as e:
            last_exc = e
            print(f'  Attempt {attempt} failed: {e}')
            if attempt < retries:
                time.sleep(delay)
    raise last_exc

try:
    r = fetch('https://httpbin.org/status/200')
    print('Success:', r.status_code)
except Exception as e:
    print('Failed:', e)

try:
    r = fetch('https://httpbin.org/status/500', retries=2, delay=0.5)
except Exception as e:
    print('Expected failure:', e)


# ---------------------------------------------------------------------------
# 3. Parse a local HTML string
# ---------------------------------------------------------------------------
HTML = """
<!DOCTYPE html>
<html>
<head><title>Tech Blog</title></head>
<body>
  <nav>
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
  </nav>
  <main>
    <article class="post">
      <h2>Getting Started with Python</h2>
      <p>Python is a versatile language great for beginners.</p>
      <p>Install Python from python.org.</p>
    </article>
    <article class="post">
      <h2>Web Scraping with BeautifulSoup</h2>
      <p>BeautifulSoup parses HTML trees elegantly.</p>
      <p>Combine it with Python requests for powerful scrapers.</p>
    </article>
    <article class="post">
      <h2>Understanding Async I/O</h2>
      <p>Async programming enables high concurrency.</p>
    </article>
  </main>
</body>
</html>
"""

soup = BeautifulSoup(HTML, 'lxml')

# a) Page title
print(soup.title.text)                                    # Tech Blog

# b) Article headlines
for h2 in soup.select('article.post h2'):
    print(h2.text)

# c) Nav links
for a in soup.select('nav a'):
    print(a['href'])                                      # /home, /about, /contact

# d) <p> tags containing "Python"
for p in soup.find_all('p'):
    if 'python' in p.text.lower():
        print(p.get_text(strip=True))


# ---------------------------------------------------------------------------
# 4. Hacker News front page
# ---------------------------------------------------------------------------
r = requests.get('https://news.ycombinator.com', timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'lxml')

stories = soup.select('span.titleline > a')
for i, story in enumerate(stories[:10], 1):
    print(f'{i}. {story.text[:70]}')
    print(f'   {story.get("href", "")}')


# ---------------------------------------------------------------------------
# 5. Table → list of dicts
# ---------------------------------------------------------------------------
TABLE_HTML = """
<table>
  <thead><tr><th>Name</th><th>Country</th><th>Score</th></tr></thead>
  <tbody>
    <tr><td>Alice</td><td>Brazil</td><td>92</td></tr>
    <tr><td>Bob</td><td>USA</td><td>87</td></tr>
    <tr><td>Carol</td><td>Germany</td><td>95</td></tr>
    <tr><td>David</td><td>Japan</td><td>78</td></tr>
  </tbody>
</table>
"""

soup = BeautifulSoup(TABLE_HTML, 'lxml')
headers = [th.text.lower() for th in soup.select('thead th')]
rows = []
for tr in soup.select('tbody tr'):
    cells = [td.text for td in tr.select('td')]
    rows.append(dict(zip(headers, cells)))

for row in rows:
    print(row)
