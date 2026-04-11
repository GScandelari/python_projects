# Mini-Project 03 — File Organizer

## Description

A script that scans a folder and organizes files into subfolders by category (images, documents, code, etc.). Fully configurable via JSON, with a dry-run mode and operation log.

## Concepts Used

| Concept | Where |
|---|---|
| `03-file-handling` | `pathlib`, `shutil`, JSON config, log file |
| `04-error-handling` | `PermissionError`, `FileExistsError`, custom exceptions |
| `02-modules-packages` | `pathlib`, `shutil`, `json`, `datetime`, `os` |
| `01-oop` | `FileOrganizer` class |

## How to Run

```bash
# Organize a folder (moves files)
python main.py /path/to/messy/folder

# Preview only — no files are moved
python main.py /path/to/messy/folder --dry-run

# Use a custom config file
python main.py /path/to/folder --config my_config.json
```

## Default Category Mapping

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.xlsx`, `.csv` |
| Code | `.py`, `.js`, `.ts`, `.html`, `.css`, `.json`, `.yaml` |
| Audio | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| Video | `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv` |
| Archives | `.zip`, `.tar`, `.gz`, `.rar`, `.7z` |
| Others | Everything else |

## Features

- Moves (or copies) files into category subfolders
- Dry-run mode: shows what would happen without touching files
- Skips subfolders (only processes files at the top level)
- Handles filename conflicts (auto-renames: `file(1).txt`, `file(2).txt`)
- Writes a timestamped log to `organizer.log`
- Config saved/loaded from `organizer_config.json`
- Custom exceptions: `OrganizerError`, `InvalidTargetError`

## Example Output (dry-run)

```
=== FILE ORGANIZER (DRY RUN) ===
Target: C:/Users/scand/Downloads

[DRY RUN] report.pdf       → Documents/report.pdf
[DRY RUN] photo.jpg        → Images/photo.jpg
[DRY RUN] script.py        → Code/script.py
[DRY RUN] song.mp3         → Audio/song.mp3
[DRY RUN] notes.txt        → Documents/notes.txt

Summary: 5 files would be moved
  Documents : 2
  Images    : 1
  Code      : 1
  Audio     : 1
```
