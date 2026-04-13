"""
Requests & BeautifulSoup — Easy Exercises
==========================================
Topics: GET requests, status codes, response data, public JSON APIs.

All exercises use public APIs that require no authentication.

Run:  python 01-easy.py
"""

import requests


# ---------------------------------------------------------------------------
# 1. Basic GET request
# ---------------------------------------------------------------------------
# Make a GET request to https://httpbin.org/get
# Print:
#   a) The status code
#   b) The 'url' field from the JSON response
#   c) Whether the request was successful (r.ok)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Query parameters
# ---------------------------------------------------------------------------
# Make a GET request to https://httpbin.org/get with these query params:
#   name='Alice', language='Python', level=3
#
# Print the 'args' field from the JSON response.
# Verify that the URL contains your parameters (print r.url).

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Response headers
# ---------------------------------------------------------------------------
# Make a GET request to https://httpbin.org/response-headers
# with query params:  X-Custom-Header=hello  and  Content-Type=application/json
#
# Print all response headers as key→value pairs.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Status codes
# ---------------------------------------------------------------------------
# httpbin can return any status code you ask for.
# For each code in [200, 201, 301, 400, 404, 500]:
#   - Make a GET request to https://httpbin.org/status/<code>
#   - Print: "200: OK (ok=True)" / "404: NOT OK (ok=False)"
# Do NOT let errors crash the loop — catch any exception.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Public JSON API — PokeAPI
# ---------------------------------------------------------------------------
# GET https://pokeapi.co/api/v2/pokemon/ditto
# Print:
#   a) The Pokémon's name
#   b) Its base experience
#   c) The names of its first 3 abilities

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Download and inspect content
# ---------------------------------------------------------------------------
# GET https://httpbin.org/image/png  (returns a PNG image)
# a) Print the Content-Type header
# b) Print the size in bytes (len(r.content))
# c) Save the image to 'downloaded.png' using binary write

# YOUR CODE HERE
