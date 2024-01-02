#!/usr/bin/env python
"""
Natural-looking commits for 2024-01-01 … 2025-06-28

Strategy
--------
1. Pre-pick 2–5 vacation blocks (each 7–14 days) + 25 % silent weeks.
2. During regular weeks:
      • 50 % chance a weekday is chosen for commits
      • chosen day gets 1–6 commits (weighted towards fewer)
The result is an irregular grid with unmistakable breaks.
"""

from __future__ import annotations
import os, random, subprocess
from datetime import date, datetime, timedelta

# ── CONFIG ────────────────────────────────────────────────────────────────────
REPO_PATH = os.path.abspath(os.path.dirname(__file__))
START, END = date(2024, 1, 1), date(2025, 6, 28)

COMMIT_WEIGHT = {1: 0.45, 2: 0.30, 3: 0.12, 4: 0.08, 5: 0.04, 6: 0.01}
SILENT_WEEK_PROB = 0.25               # 25 % ISO weeks entirely blank
VACATION_BLOCKS = random.randint(2, 5)  # how many long breaks
BLOCK_MIN, BLOCK_MAX = 7, 14          # block length days
WORK_HOURS = range(8, 22)             # 08 h .. 21 h timestamps
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")
# ──────────────────────────────────────────────────────────────────────────────


def git(*args: str, env: dict | None = None) -> None:
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)


def random_ts(d: date) -> str:
    dt = datetime(
        d.year, d.month, d.day,
        random.choice(WORK_HOURS),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def weighted_commit_count() -> int:
    r, cum = random.random(), 0.0
    for k, w in COMMIT_WEIGHT.items():
        cum += w
        if r <= cum:
            return k
    return 1


# Build vacation day set
vacation_days: set[date] = set()
cursor = START
all_days = (END - START).days
for _ in range(VACATION_BLOCKS):
    block_start = START + timedelta(days=random.randint(0, all_days))
    block_len = random.randint(BLOCK_MIN, BLOCK_MAX)
    for i in range(block_len):
        vacation_days.add(block_start + timedelta(days=i))

# Pick silent ISO weeks
silent_weeks = {wk for wk in range(1, 54) if random.random() < SILENT_WEEK_PROB}

print(f"🏖  Long-break days: {len(vacation_days)}")
print(f"🛑 Silent weeks (ISO): {sorted(silent_weeks)}")

# Main loop
day = START
while day <= END:
    iso = day.isocalendar()
    if (
        day in vacation_days
        or iso.week in silent_weeks
        or iso.weekday >= 6            # skip weekends
        or random.random() > 0.5       # 50 % of weekdays stay blank
    ):
        day += timedelta(days=1)
        continue

    commits_today = weighted_commit_count()
    for _ in range(commits_today):
        with open(TARGET_FILE, "a", encoding="utf-8") as fh:
            fh.write(f"# auto-log {day.isoformat()} {random.randint(1000,9999)}\n")

        ts = random_ts(day)
        env = {**os.environ,
               "GIT_AUTHOR_DATE": ts,
               "GIT_COMMITTER_DATE": ts}

        git("add", ".")
        git("commit", "-m", f"chore(auto-log): {ts}", env=env)

    day += timedelta(days=1)

print("\n✅ Natural commits created — push with:")
print("   git push origin main")
