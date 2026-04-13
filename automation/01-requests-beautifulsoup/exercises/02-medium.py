"""
Requests & BeautifulSoup — Medium Exercises
============================================
Topics: Session, error handling with retries, BeautifulSoup HTML parsing,
        CSS selectors, extracting structured data.

Run:  python 02-medium.py
"""

import requests
from bs4 import BeautifulSoup
import time


# ---------------------------------------------------------------------------
# 1. Session with shared headers
# ---------------------------------------------------------------------------
# Create a requests.Session with these default headers:
#   User-Agent: 'PythonScraper/1.0'
#   Accept: 'application/json'
#
# Use the session to make two requests to httpbin.org/headers
# and httpbin.org/get.
# Print the 'headers' field from each response.
# Confirm that your custom headers appear in both.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Robust fetcher with retry
# ---------------------------------------------------------------------------
# Implement fetch(url, retries=3, delay=1.0) that:
#   - Makes a GET request with timeout=10
#   - On any exception (Timeout, ConnectionError, HTTPError from 5xx),
#     waits `delay` seconds and retries up to `retries` times
#   - Returns the Response object on success
#   - Raises the last exception if all retries fail
#
# Test it against:
#   https://httpbin.org/status/200  (should succeed first try)
#   https://httpbin.org/status/500  (should retry and eventually raise)

def fetch(url, retries=3, delay=1.0):
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# 3. Parse a local HTML string
# ---------------------------------------------------------------------------
# Given the HTML below, extract and print:
# a) The page title (inside <title>)
# b) All article headlines (h2 inside article.post)
# c) All href values of links inside nav
# d) The text of every <p> tag that contains the word "Python"

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

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Scrape a live page — Hacker News front page
# ---------------------------------------------------------------------------
# Fetch https://news.ycombinator.com (HN front page)
# Extract and print the top 10 stories:
#   - Title text
#   - URL (href of the title link)
#
# Hint: story titles are in <span class="titleline"> → <a> tag

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Extract a table into a list of dicts
# ---------------------------------------------------------------------------
# Given the HTML table below, parse it into a list of dicts where
# each dict has keys matching the column headers (lowercase).
# Print each dict.

TABLE_HTML = """
<table>
  <thead>
    <tr><th>Name</th><th>Country</th><th>Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Alice</td><td>Brazil</td><td>92</td></tr>
    <tr><td>Bob</td><td>USA</td><td>87</td></tr>
    <tr><td>Carol</td><td>Germany</td><td>95</td></tr>
    <tr><td>David</td><td>Japan</td><td>78</td></tr>
  </tbody>
</table>
"""

# YOUR CODE HERE
