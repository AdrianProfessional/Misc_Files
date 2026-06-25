#!/usr/bin/env python3
"""
GitHub Activity Filler
Generates 5–10 random coding files daily and pushes them to a GitHub repo.
"""

import os
import random
import string
import subprocess
from datetime import datetime
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────────────────────────
REPO_PATH = "C:\\Misc_Files"   # ← Change this to your local git repo path
COMMIT_AUTHOR_NAME = "AdrianProfessional"          # ← Your GitHub name
COMMIT_AUTHOR_EMAIL = "adriaanr60@gmail.com"    # ← Your GitHub email
# ───────────────────────────────────────────────────────────────────────────────

# ── File generators ─────────────────────────────────────────────────────────────
 
def rand_name(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
 
def rand_words(n=3):
    words = ["process", "fetch", "parse", "load", "build", "run", "check",
             "sync", "update", "validate", "filter", "map", "reduce", "sort",
             "merge", "split", "encode", "decode", "format", "convert"]
    return random.sample(words, min(n, len(words)))
 
def make_python():
    fn_names = rand_words(random.randint(2, 4))
    lines = [
        "import os",
        "import json",
        "from datetime import datetime",
        "",
    ]
    for fn in fn_names:
        arg = rand_name(4)
        body_lines = [
            f'    """Auto-generated utility: {fn}."""',
            f"    result = []",
            f"    for item in {arg}:",
            f"        if item:",
            f"            result.append(str(item).strip())",
            f"    return result",
        ]
        lines += [f"def {fn}({arg}):", *body_lines, ""]
    lines += [
        'if __name__ == "__main__":',
        f'    print("Module loaded:", __file__)',
    ]
    return "\n".join(lines), f"{rand_name()}_utils.py"
 
def make_javascript():
    fn_names = rand_words(random.randint(2, 4))
    lines = ["'use strict';", ""]
    for fn in fn_names:
        arg = rand_name(4)
        lines += [
            f"/**",
            f" * {fn} — auto-generated helper",
            f" * @param {{{arg}}} items",
            f" */",
            f"function {fn}({arg}) {{",
            f"  if (!Array.isArray({arg})) return [];",
            f"  return {arg}.filter(Boolean).map(x => x.toString().trim());",
            f"}}",
            "",
        ]
    lines += [f"module.exports = {{ {', '.join(fn_names)} }};"]
    return "\n".join(lines), f"{rand_name()}_helpers.js"
 
def make_bash():
    action = random.choice(rand_words(1))
    lines = [
        "#!/usr/bin/env bash",
        f"# Auto-generated script: {action}",
        "set -euo pipefail",
        "",
        f'LOG_FILE="/tmp/{rand_name()}.log"',
        "",
        f"echo '[INFO] Starting {action} — $(date)'",
        "",
        "cleanup() {",
        '  echo "[INFO] Cleanup complete."',
        "}",
        "trap cleanup EXIT",
        "",
        "# Main",
        f'echo "[INFO] Running {action}..." | tee -a "$LOG_FILE"',
        'echo "[DONE] Finished."',
    ]
    return "\n".join(lines), f"{rand_name()}.sh"
 
def make_sql():
    table = rand_name(5) + "s"
    cols = [(rand_name(4), t) for t in random.sample(
        ["VARCHAR(255)", "INT", "BOOLEAN", "TIMESTAMP", "TEXT", "DECIMAL(10,2)"],
        k=random.randint(3, 5)
    )]
    lines = [
        f"-- Auto-generated schema: {table}",
        f"CREATE TABLE IF NOT EXISTS {table} (",
        "  id SERIAL PRIMARY KEY,",
    ]
    for col, dtype in cols:
        lines.append(f"  {col} {dtype},")
    lines += [
        "  created_at TIMESTAMP DEFAULT NOW()",
        ");",
        "",
        f"-- Indexes",
        f"CREATE INDEX IF NOT EXISTS idx_{table}_created ON {table}(created_at);",
        "",
        f"-- Sample query",
        f"SELECT * FROM {table} WHERE created_at > NOW() - INTERVAL '7 days' ORDER BY created_at DESC LIMIT 50;",
    ]
    return "\n".join(lines), f"{rand_name()}_schema.sql"
 
def make_typescript():
    type_name = rand_name(5).capitalize()
    fn_names = rand_words(random.randint(2, 3))
    lines = [
        f"// Auto-generated TypeScript module",
        "",
        f"interface {type_name} {{",
        f"  id: string;",
        f"  value: number;",
        f"  label: string;",
        f"  active: boolean;",
        f"}}",
        "",
    ]
    for fn in fn_names:
        lines += [
            f"export function {fn}(items: {type_name}[]): {type_name}[] {{",
            f"  return items.filter(item => item.active).sort((a, b) => a.value - b.value);",
            f"}}",
            "",
        ]
    return "\n".join(lines), f"{rand_name()}.ts"
 
def make_markdown():
    topic = random.choice(rand_words(1)).capitalize()
    lines = [
        f"# {topic} Notes",
        "",
        f"Auto-generated notes on **{topic}** — {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Overview",
        f"This document covers key concepts related to {topic}.",
        "",
        "## Key Points",
        f"- Point one about {topic}",
        f"- Point two about {topic}",
        f"- Point three about {topic}",
        "",
        "## References",
        "- https://docs.example.com",
    ]
    return "\n".join(lines), f"{rand_name()}_notes.md"
 
GENERATORS = [make_python, make_javascript, make_bash, make_sql, make_typescript, make_markdown]
 
# ── Core logic ──────────────────────────────────────────────────────────────────
 
def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()
 
def main():
    repo = Path(REPO_PATH)
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"No git repo found at: {repo}")
 
    # Pull latest (skip if repo has no commits yet)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True)
    has_commits = result.returncode == 0
    if has_commits:
        run(["git", "pull", "--rebase"], cwd=repo)
 
    count = random.randint(5, 10)
    chosen = random.choices(GENERATORS, k=count)
 
    # Use a dated subfolder so files don't clog the root
    date_str = datetime.now().strftime("%Y/%m/%d")
    target_dir = repo / "daily" / date_str
    target_dir.mkdir(parents=True, exist_ok=True)
 
    files_added = []
    for gen in chosen:
        content, filename = gen()
        # Avoid collisions if same filename generated twice
        filepath = target_dir / filename
        if filepath.exists():
            stem, ext = os.path.splitext(filename)
            filename = f"{stem}_{rand_name(3)}{ext}"
            filepath = target_dir / filename
        filepath.write_text(content)
        files_added.append(str(filepath.relative_to(repo)))
        print(f"  Created: {filepath.relative_to(repo)}")
 
    # Stage and commit
    run(["git", "add", "."], cwd=repo)
 
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = COMMIT_AUTHOR_NAME
    env["GIT_AUTHOR_EMAIL"] = COMMIT_AUTHOR_EMAIL
    env["GIT_COMMITTER_NAME"] = COMMIT_AUTHOR_NAME
    env["GIT_COMMITTER_EMAIL"] = COMMIT_AUTHOR_EMAIL
 
    commit_messages = [
        f"chore: add daily utility scripts ({count} files)",
        f"feat: scaffold {count} helper modules",
        f"refactor: add auto-generated utilities for {datetime.now().strftime('%b %d')}",
        f"docs: update notes and helpers ({count} files)",
        f"build: include {count} generated scripts",
    ]
    msg = random.choice(commit_messages)
 
    subprocess.run(
        ["git", "commit", "-m", msg],
        cwd=repo, env=env, check=True
    )
    run(["git", "push"], cwd=repo)
 
    print(f"\n✓ Pushed {count} files to GitHub: {msg}")
 
if __name__ == "__main__":
    main()
 