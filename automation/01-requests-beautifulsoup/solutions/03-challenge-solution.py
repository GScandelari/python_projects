"""
Requests & BeautifulSoup — Challenge Solutions
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
from urllib.parse import urljoin, urlparse


RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


# ---------------------------------------------------------------------------
# 1. Multi-page scraper — Books to Scrape
# ---------------------------------------------------------------------------
def scrape_books(num_pages=3):
    books = []
    base = 'https://books.toscrape.com/catalogue/page-{}.html'
    with requests.Session() as s:
        s.headers.update({'User-Agent': 'PythonScraper/1.0'})
        for page in range(1, num_pages + 1):
            r = s.get(base.format(page), timeout=10)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'lxml')
            for article in soup.select('article.product_pod'):
                price_str = article.select_one('.price_color').text.strip()
                price = float(price_str.replace('£', '').replace('Â', ''))
                rating_word = article.p['class'][1]
                avail = article.select_one('.availability').get_text(strip=True)
                books.append({
                    'title':        article.h3.a['title'],
                    'price':        price,
                    'rating':       RATING_MAP.get(rating_word, 0),
                    'availability': avail,
                })
            if page < num_pages:
                time.sleep(0.5)
    return books

books = scrape_books(3)
print(f'Scraped {len(books)} books')
if books:
    avg = sum(b['price'] for b in books) / len(books)
    print(f'Average price: £{avg:.2f}')


# ---------------------------------------------------------------------------
# 2. Export to CSV and JSON
# ---------------------------------------------------------------------------
def export_csv(books, filename='books.csv'):
    if not books:
        return
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'rating', 'availability'])
        writer.writeheader()
        writer.writerows(books)
    print(f'Exported {len(books)} books to {filename}')

def export_json(books, filename='books.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
    print(f'Exported {len(books)} books to {filename}')

def top_rated(filename='books.csv', n=5):
    rows = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['rating'] = int(row['rating'])
            rows.append(row)
    rows.sort(key=lambda r: r['rating'], reverse=True)
    return rows[:n]

if books:
    export_csv(books)
    export_json(books)
    top = top_rated()
    print('\nTop 5 rated books:')
    for b in top:
        print(f"  [{b['rating']}★] {b['title']}")


# ---------------------------------------------------------------------------
# 3. Paginated REST API
# ---------------------------------------------------------------------------
BASE = 'https://jsonplaceholder.typicode.com'

with requests.Session() as s:
    # a) Longest post body
    posts = s.get(f'{BASE}/posts', timeout=10).json()
    longest = max(posts, key=lambda p: len(p['body']))
    print(f'\nLongest post title: {longest["title"]}')

    # b) Comments per post (1–3)
    for post_id in [1, 2, 3]:
        comments = s.get(f'{BASE}/posts/{post_id}/comments', timeout=10).json()
        print(f'Post {post_id}: {len(comments)} comments')

    # c) {post_id: [emails]} for posts 1–5
    email_map = {}
    for post_id in range(1, 6):
        comments = s.get(f'{BASE}/posts/{post_id}/comments', timeout=10).json()
        email_map[post_id] = [c['email'] for c in comments]

    for pid, emails in email_map.items():
        print(f'Post {pid}: {emails[:2]}...')


# ---------------------------------------------------------------------------
# 4. Simple link crawler
# ---------------------------------------------------------------------------
def crawl(start_url, max_pages=10):
    visited = set()
    queue   = [start_url]
    results = []
    domain  = urlparse(start_url).netloc

    with requests.Session() as s:
        s.headers.update({'User-Agent': 'PythonCrawler/1.0'})
        while queue and len(visited) < max_pages:
            url = queue.pop(0)
            if url in visited:
                continue
            try:
                r = s.get(url, timeout=10)
                r.raise_for_status()
            except Exception as e:
                print(f'  Skip {url}: {e}')
                continue

            visited.add(url)
            soup = BeautifulSoup(r.text, 'lxml')
            title = soup.title.text.strip() if soup.title else ''
            links = []
            for a in soup.find_all('a', href=True):
                abs_url = urljoin(url, a['href'])
                parsed  = urlparse(abs_url)
                if parsed.netloc == domain and parsed.scheme in ('http', 'https'):
                    links.append(abs_url)
                    if abs_url not in visited:
                        queue.append(abs_url)

            results.append({'url': url, 'title': title, 'num_links': len(links)})
            time.sleep(0.5)

    return results

results = crawl('https://books.toscrape.com', max_pages=5)
for r in results:
    print(f"{r['url']} — {r['num_links']} links — {r['title'][:40]}")
