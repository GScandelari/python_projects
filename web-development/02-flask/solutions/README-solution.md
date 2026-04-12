# Flask — Solution Notes

## Easy

**`request.get_json(silent=True)`:** Without `silent=True`, Flask raises a 400 automatically if the body isn't valid JSON. With it, the method returns `None` on bad input — giving you control over the error response.

**`abort(404)` vs `return ..., 404`:** `abort()` raises an exception that propagates to the error handler. It's cleaner for flow control inside helper functions. `return jsonify(...), 404` gives more control over the response body.

**`request.args.get('key')`:** Returns `None` if the key is absent (never raises). Use a default: `request.args.get('limit', 10)`. Remember to cast — all query param values are strings.

**Route converters:** `<int:n>`, `<float:n>`, `<string:s>`, `<path:p>`. Using converters causes Flask to return 404 automatically if the type doesn't match.

## Medium

**Blueprint url_prefix:** Setting it on `Blueprint(url_prefix=...)` or `app.register_blueprint(bp, url_prefix=...)` — the latter takes precedence. Prefer setting it at `register_blueprint` for flexibility.

**204 No Content:** Return an empty string and the status code: `return '', 204`. Do not call `jsonify()` — a JSON body would conflict with the 204 semantics.

**Filtering in list endpoints:** Always apply filters on top of the base query (list of values), not by modifying the store. This keeps the store untouched and makes the logic composable.

**Validation helper:** Extracting validation into a helper (`_validate_book_payload`) keeps route functions short and makes validation reusable across POST and PUT.

## Challenge

**Application factory:** `create_app()` enables multiple instances (e.g., test vs production config). Always configure the app, register blueprints, and add handlers inside the factory — never at module level.

**`before_request`:** Runs before every request in the app (or blueprint). Return a response from it to short-circuit the actual route handler. `None` (implicit return) lets the request proceed normally.

**`flask.g`:** Per-request storage. Anything you put in `g` during `before_request` is available in the route handler for that same request. It's reset between requests.

**Pagination pattern:** `start = (page - 1) * per_page` is the universal formula. Always clamp `per_page` to a reasonable maximum in production to prevent memory exhaustion.

**Blueprints vs inline routes:** Use blueprints for anything with more than 2–3 routes. They enable per-blueprint `before_request`, `after_request`, and `errorhandler` — useful for API versioning.
