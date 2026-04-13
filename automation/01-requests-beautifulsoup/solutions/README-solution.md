# Requests & BeautifulSoup — Solution Notes

## Easy

**Always set a timeout:** `requests.get(url, timeout=10)` — without it a stalled server can block your script forever. Use `(connect_timeout, read_timeout)` for finer control: `timeout=(3, 10)`.

**`r.ok` vs `r.raise_for_status()`:** `r.ok` is a bool (True for 2xx/3xx). `raise_for_status()` raises `HTTPError` for 4xx/5xx — use it when you want the exception to propagate automatically.

**Binary content:** Use `r.content` (bytes) for images, PDFs, zips. Use `r.text` (str) for HTML/JSON/XML. `r.json()` is a shortcut for `json.loads(r.text)`.

## Medium

**Session benefits:** Reuses the underlying TCP connection (keep-alive), persists cookies automatically, and lets you set shared headers/auth once instead of repeating them on every call. Always use a Session when making multiple requests to the same host.

**`raise_for_status()` inside retry:** Call it immediately after the request so HTTP errors (4xx/5xx) trigger the retry logic the same way network errors do. Skip retrying on 4xx (client errors are not transient) in production code.

**CSS selector vs `.find()`:** Prefer `soup.select('css selector')` for complex queries (nested, multi-class, attribute). Use `soup.find('tag', class_='name')` for simple single-tag lookups. They're equivalent for simple cases — pick the one that reads more clearly.

**Table → dicts pattern:** Extract headers first, then zip each row's cells against the headers. This scales to any number of columns without hardcoding field names.

## Challenge

**Polite scraping:** Always add `time.sleep(0.5–1)` between requests. Check the site's `robots.txt` before scraping. Use a descriptive `User-Agent` so site owners can identify and contact you.

**Price cleaning:** Pages from non-English servers sometimes have encoding artifacts (`Â£` instead of `£`). Strip all non-numeric characters except `.` when parsing prices: `re.sub(r'[^\d.]', '', text)`.

**Crawler queue management:** Use a `set` for visited URLs (O(1) lookup) and a `list` as a queue (`pop(0)` for BFS). Normalise URLs before adding to the set — `urljoin` resolves relative paths, but watch for `?` and `#` fragments.

**Exporting data:** Write CSV with `csv.DictWriter` — it handles quoting automatically. Use `newline=''` when opening the file to prevent double line endings on Windows. Always set `encoding='utf-8'` for international characters.

**Pagination API pattern:** Check the `next` field (or `Link` header) in each response. `None` signals the last page. This pattern applies to GitHub API, Twitter API, and most well-designed REST APIs.
