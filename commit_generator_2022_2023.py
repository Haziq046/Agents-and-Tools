#!/usr/bin/env python
"""
Sparse back-dated commits for 2022-2023
• Commits happen every 3rd calendar day
• 1–3 commits on those days
• No activity on the other two days
"""

from __future__ import annotations
import os
import random
import subprocess
from datetime import date, datetime, timedelta


# ── CONFIG ────────────────────────────────────────────────────────────────────
REPO_PATH   = os.path.abspath(os.path.dirname(__file__))      # repo root
START_DATE  = date(2022, 2, 1)
END_DATE    = date(2023, 12, 31)
FREQUENCY   = 3                            # one batch every N days
COMMITS_PER_BATCH = (1, 3)                 # inclusive range
WORK_HOURS = range(9, 18)                  # 09:00-17:59
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")    # file to touch
# ──────────────────────────────────────────────────────────────────────────────


def git(*args: str, env: dict | None = None) -> None:
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)


def rand_timestamp(d: date) -> str:
    """Return random timestamp (ISO-like) within work hours on date *d*."""
    dt = datetime(
        d.year, d.month, d.day,
        random.choice(WORK_HOURS),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def main() -> None:
    os.chdir(REPO_PATH)
    print(f"Repo ➜ {REPO_PATH}")

    day: date = START_DATE
    while day <= END_DATE:
        # commit batch on this day
        num_commits = random.randint(*COMMITS_PER_BATCH)

        for _ in range(num_commits):
            # append a trivial change so the commit isn’t empty
            with open(TARGET_FILE, "a", encoding="utf-8") as fh:
                fh.write(f"# auto-log {day.isoformat()} {random.randint(1000, 9999)}\n")

            ts = rand_timestamp(day)
            env = {**os.environ,
                   "GIT_AUTHOR_DATE": ts,
                   "GIT_COMMITTER_DATE": ts}

            git("add", ".")
            git("commit", "-m", f"chore(auto-log): {ts}", env=env)

        # jump ahead three days
        day += timedelta(days=FREQUENCY)

    print("✅ Commits generated — push with:")
    print("   git push origin main")


if __name__ == "__main__":
    main()
