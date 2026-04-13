# Automation — Solution Notes

## Easy

**`exist_ok=True`:** Always pass it to `mkdir` in automation scripts — re-running a script shouldn't fail just because the directory already exists.

**`write_text` / `read_text`:** Always pass `encoding='utf-8'` explicitly. Without it, Python uses the system default encoding, which differs between Windows (cp1252) and Linux (UTF-8), causing hard-to-reproduce bugs.

**`shutil.rmtree(ignore_errors=True)`:** Safer than the default for cleanup in scripts — a missing directory or locked file won't abort the whole script.

**CSV `newline=''`:** Required when opening a file for `csv.writer`. Without it, Python's universal newline translation on Windows produces blank lines between each row.

## Medium

**Extension map pattern:** A `dict` mapping suffix → category scales easily — add a new rule without changing any logic. `file.suffix.lower()` normalises `.PNG` to `.png` so the map stays simple.

**`subprocess.run` vs `os.system`:** Always prefer `subprocess.run`. It captures output, doesn't depend on the shell, avoids injection, and returns a structured result. Use `check=True` to raise automatically on non-zero exit codes.

**`os.walk` vs `pathlib.rglob`:** Both traverse recursively. `os.walk` gives (`dirpath`, `dirnames`, `filenames`) — useful when you need to modify `dirnames` to prune the traversal. `rglob('*')` is more Pythonic for read-only traversal.

**Multiple logging handlers:** Use `logger.addHandler()` to attach both a `FileHandler` and a `StreamHandler`. Set the logger's level to the lowest you need (`DEBUG`) and let each handler's level filter further.

## Challenge

**Timestamped backup:** `datetime.now().strftime('%Y-%m-%d_%H-%M-%S')` produces a sortable, filesystem-safe timestamp. Lexicographic sort gives chronological order automatically — useful for finding the latest backup with `sorted(backups)[-1]`.

**MD5 for file comparison:** Fast and collision-resistant enough for comparing local files. For security-sensitive contexts use SHA-256. Reading the entire file into memory (`path.read_bytes()`) is fine for most automation; for very large files use `hashlib.md5()` in 64KB chunks.

**Sync relative paths:** Computing `f.relative_to(src)` allows the same relative structure to be replicated in the target. This is the key to a faithful mirror — never use just the filename, or you'll collapse the subdirectory structure.

**`fnmatch.fnmatch`:** Shell-style pattern matching (`*.log`, `data_*.csv`). Always match against `file.name` (not the full path) unless you intend to match directory components too.

**Config-driven automation:** Separating rules from code (JSON config) means non-programmers can modify behaviour without touching Python. The processor becomes a general engine; the config becomes the specification.
