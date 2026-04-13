"""
Requests & BeautifulSoup — Challenge Exercises
===============================================
Topics: multi-page scraper, pagination, rate limiting, CSV/JSON export,
        link crawler, data cleaning.

Run:  python 03-challenge.py
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time


# ---------------------------------------------------------------------------
# 1. Multi-page scraper — Books to Scrape
# ---------------------------------------------------------------------------
# Scrape the first 3 pages of https://books.toscrape.com
# Each page URL follows the pattern:
#   https://books.toscrape.com/catalogue/page-{n}.html
#
# For each book, collect:
#   title, price (as float, strip the £ sign), rating (word → number),
#   availability (strip whitespace)
#
# Rating words: One=1, Two=2, Three=3, Four=4, Five=5
#
# Print a summary: total books scraped, average price.
# Wait 0.5 seconds between page requests.

RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

def scrape_books(num_pages=3):
    # YOUR CODE HERE
    pass

books = scrape_books(3)
if books:
    print(f'Scraped {len(books)} books')
    avg = sum(b['price'] for b in books) / len(books)
    print(f'Average price: £{avg:.2f}')


# ---------------------------------------------------------------------------
# 2. Export to CSV and JSON
# ---------------------------------------------------------------------------
# Using the books list from exercise 1:
# a) Export to 'books.csv' with headers: title, price, rating, availability
# b) Export to 'books.json' (pretty-printed with indent=2)
# c) Read the CSV back and print the 5 highest-rated books (sort by rating desc)

def export_csv(books, filename='books.csv'):
    # YOUR CODE HERE
    pass

def export_json(books, filename='books.json'):
    # YOUR CODE HERE
    pass

def top_rated(filename='books.csv', n=5):
    # YOUR CODE HERE — read CSV, sort, return top n
    pass


# ---------------------------------------------------------------------------
# 3. Paginated REST API
# ---------------------------------------------------------------------------
# The JSONPlaceholder API (https://jsonplaceholder.typicode.com) has:
#   GET /posts         → 100 posts
#   GET /comments      → 500 comments
#   GET /posts/{id}/comments → comments for one post
#
# a) Fetch all 100 posts and print the title of the longest post body.
# b) For posts with id 1, 2, and 3, fetch their comments concurrently
#    using a Session and print the total comment count for each.
# c) Build a dict {post_id: [list of commenter emails]} for posts 1–5.

BASE = 'https://jsonplaceholder.typicode.com'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Simple link crawler
# ---------------------------------------------------------------------------
# Implement crawl(start_url, max_pages=10) that:
#   - Starts at start_url
#   - Extracts all <a href="..."> links on the page
#   - Visits unvisited links that belong to the same domain
#   - Stops when max_pages have been visited
#   - Returns a list of dicts: {url, title, num_links}
#
# Test with: crawl('https://books.toscrape.com', max_pages=5)
# Wait 0.5s between requests.

from urllib.parse import urljoin, urlparse

def crawl(start_url, max_pages=10):
    # YOUR CODE HERE
    pass

results = crawl('https://books.toscrape.com', max_pages=5)
for r in results:
    print(f"{r['url']} — {r['num_links']} links")
