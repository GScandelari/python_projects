# ============================================================
# Intermediate Mini-Project 03 — File Organizer (SOLUTION)
# ============================================================

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime


# ── Custom Exceptions ─────────────────────────────────────

class OrganizerError(Exception):
    pass

class InvalidTargetError(OrganizerError):
    def __init__(self, path):
        super().__init__(f"Target is not a valid directory: '{path}'")


# ── FileOrganizer ─────────────────────────────────────────

class FileOrganizer:
    DEFAULT_CATEGORIES = {
        "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".xlsx", ".csv"],
        "Code":      [".py", ".js", ".ts", ".html", ".css", ".json", ".yaml", ".yml"],
        "Audio":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Video":     [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
        "Archives":  [".zip", ".tar", ".gz", ".rar", ".7z"],
    }
    OTHER_CATEGORY = "Others"

    def __init__(self, target_dir, dry_run=False, config_path=None):
        self.target = Path(target_dir).resolve()
        if not self.target.is_dir():
            raise InvalidTargetError(target_dir)

        self.dry_run = dry_run
        self.log_path = self.target / "organizer.log"

        # Build reverse map: extension (lowercase) → category
        categories = self.DEFAULT_CATEGORIES.copy()
        if config_path:
            self.load_config(config_path, categories)
        self.ext_map = {}
        for category, extensions in categories.items():
            for ext in extensions:
                self.ext_map[ext.lower()] = category

    def get_category(self, extension):
        return self.ext_map.get(extension.lower(), self.OTHER_CATEGORY)

    def resolve_conflict(self, dest_path):
        dest = Path(dest_path)
        if not dest.exists():
            return dest
        stem = dest.stem
        suffix = dest.suffix
        parent = dest.parent
        counter = 1
        while True:
            candidate = parent / f"{stem}({counter}){suffix}"
            if not candidate.exists():
                return candidate
            counter += 1

    def _move_file(self, src, dest):
        dest = self.resolve_conflict(dest)
        if self.dry_run:
            rel_dest = dest.relative_to(self.target)
            msg = f"[DRY RUN] {src.name:<30} → {rel_dest}"
            print(f"  {msg}")
            self._log(msg)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            rel_dest = dest.relative_to(self.target)
            msg = f"[MOVED]   {src.name:<30} → {rel_dest}"
            print(f"  {msg}")
            self._log(msg)
        return dest

    def _log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def organize(self):
        summary = {}
        files = [f for f in self.target.iterdir() if f.is_file()
                 and f.name != "organizer.log"]

        if not files:
            print("  No files to organize.")
            return summary

        mode = "DRY RUN" if self.dry_run else "ORGANIZING"
        header = f"=== FILE ORGANIZER ({mode}) ==="
        print(f"\n{header}")
        print(f"Target: {self.target}\n")
        self._log(header)
        self._log(f"Target: {self.target}")

        for src in sorted(files):
            ext = src.suffix.lower()
            category = self.get_category(ext)
            dest = self.target / category / src.name
            self._move_file(src, dest)
            summary.setdefault(category, []).append(src.name)

        self._print_summary(summary)
        return summary

    def _print_summary(self, summary):
        total = sum(len(v) for v in summary.values())
        action = "would be moved" if self.dry_run else "moved"
        print(f"\nSummary: {total} file(s) {action}")
        for category, files in sorted(summary.items()):
            print(f"  {category:<12}: {len(files)}")

    def save_config(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.DEFAULT_CATEGORIES, f, indent=2)
        print(f"Config saved to {path}")

    def load_config(self, path, categories):
        try:
            with open(path, "r", encoding="utf-8") as f:
                custom = json.load(f)
            categories.update(custom)
        except FileNotFoundError:
            print(f"  Config not found: {path} — using defaults.")
        except json.JSONDecodeError as e:
            raise OrganizerError(f"Invalid config JSON: {e}") from e


# ── Entry Point ───────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python solution.py <target_folder> [--dry-run] [--config <path>]")
        print("\nExample (current directory):")
        # Demo with current directory
        target = os.path.dirname(__file__)
    else:
        target = args[0]

    dry_run = "--dry-run" in args
    config_path = None
    if "--config" in args:
        idx = args.index("--config")
        try:
            config_path = args[idx + 1]
        except IndexError:
            print("Error: --config requires a path argument.")
            sys.exit(1)

    try:
        organizer = FileOrganizer(target, dry_run=dry_run, config_path=config_path)
        organizer.organize()
    except OrganizerError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
