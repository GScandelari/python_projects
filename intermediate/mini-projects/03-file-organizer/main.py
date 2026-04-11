# ============================================================
# Intermediate Mini-Project 03 — File Organizer
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Build the category config first (dict: extension -> category)
#   3. Implement the FileOrganizer class step by step
#   4. Add dry-run mode (same logic, just skip the actual move)
#   5. Add logging last
#   6. Check solution.py only after you have a working version
#
# SUGGESTED CLASS STRUCTURE:
#
# class OrganizerError(Exception): ...
# class InvalidTargetError(OrganizerError): ...
#
# class FileOrganizer:
#     DEFAULT_CATEGORIES = {
#         "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
#         "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".xlsx", ".csv"],
#         "Code":      [".py", ".js", ".ts", ".html", ".css", ".json", ".yaml"],
#         "Audio":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
#         "Video":     [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
#         "Archives":  [".zip", ".tar", ".gz", ".rar", ".7z"],
#     }
#     OTHER_CATEGORY = "Others"
#
#     def __init__(self, target_dir, dry_run=False, config_path=None):
#         # validate target_dir exists and is a directory
#         # load config from config_path if provided, else use DEFAULT_CATEGORIES
#         # build reverse map: extension -> category
#
#     def get_category(self, extension): ...
#         # returns category name for given extension (lowercase)
#
#     def resolve_conflict(self, dest_path): ...
#         # if dest_path exists, append (1), (2), etc. until unique
#
#     def organize(self): ...
#         # scans target_dir, moves (or dry-runs) each file
#         # returns summary dict {category: [filenames]}
#
#     def _move_file(self, src, dest): ...
#         # in dry-run: just log. otherwise: dest.parent.mkdir + shutil.move
#
#     def _log(self, message): ...
#         # appends timestamped message to organizer.log
#
#     def save_config(self, path): ...
#     def load_config(self, path): ...
#
# CONFLICT RESOLUTION:
#   If "photo.jpg" already exists in Images/:
#   Try "photo(1).jpg", "photo(2).jpg", etc.
#   Use: Path(dest).stem + "(N)" + Path(dest).suffix
#
# USAGE (from command line):
#   python main.py <target_folder> [--dry-run] [--config config.json]
#
# Parse sys.argv manually (no argparse needed):
#   sys.argv[1] = target folder
#   "--dry-run" in sys.argv → dry_run = True
#   "--config" in sys.argv → next element is config path
# ============================================================

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

# Write your code here


if __name__ == "__main__":
    main()
