#!/usr/bin/env python
"""
Organic back-dated commit generator

Mood model
----------
The script keeps a daily *mood* state:
    • QUIET   → 0-1 commits
    • NORMAL  → 1-4 commits
    • FOCUS   → 4-8 commits

Prob(stay in same mood) starts high (0.75) and decays by 0.05 each day,
so streaks naturally end.  When it switches, the next mood is picked
weighted toward ~NORMAL but can jump to any state.

Weekends are skipped, and about 1 in 10 ISO weeks is a full vacation.
Adjust constants at top to tune behaviour.

Run once, then `git push origin main`.
"""

from __future__ import annotations
import os
import random
import subprocess
from datetime import date, datetime, timedelta

# ── CONFIG ────────────────────────────────────────────────────────────────────
REPO_PATH = os.path.abspath(os.path.dirname(__file__))  # repo root
START_DATE = date(2024, 1, 1)
END_DATE   = date.today()
WORK_HOURS = range(9, 18)                # commits between 09-17
VACATION_WEEK_PROB = 0.10                # 10 % of weeks skipped
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")
# ──────────────────────────────────────────────────────────────────────────────

# Mood → (min, max) commit counts
QUIET   = (0, 1)
NORMAL  = (1, 4)
FOCUS   = (4, 8)
MOODS   = [QUIET, NORMAL, FOCUS]

def git(*args: str, env: dict | None = None) -> None:
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)

def rand_ts(day: date) -> str:
    """Random ISO-like timestamp during work hours."""
    dt = datetime(
        day.year, day.month, day.day,
        random.choice(WORK_HOURS),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

# Create a set of “vacation” ISO week numbers
vacation_weeks: set[int] = {
    w for w in range(1, 54) if random.random() < VACATION_WEEK_PROB
}

print(f"📆 Vacation weeks (ISO): {sorted(vacation_weeks)}")

# mood state & probability to stay
current_mood_idx = 1                 # start at NORMAL
stay_prob = 0.75                     # 75 % chance to repeat first day

day = START_DATE
while day <= END_DATE:
    iso = day.isocalendar()
    if iso.week in vacation_weeks or iso.weekday >= 6:   # weekend/vacation
        day += timedelta(days=1)
        continue

    # decide if mood changes
    if random.random() > stay_prob:
        # pick a new mood with weighted choice
        current_mood_idx = random.choices(
            population=[0, 1, 2],
            weights=[0.25, 0.5, 0.25],   # bias toward NORMAL
            k=1
        )[0]
        stay_prob = 0.75                # reset streak stickiness
    else:
        stay_prob = max(0.3, stay_prob - 0.05)   # decay

    commit_range = MOODS[current_mood_idx]
    commits_today = random.randint(*commit_range)

    for _ in range(commits_today):
        # mutate a line
        with open(TARGET_FILE, "a", encoding="utf-8") as fh:
            fh.write(f"# auto-log {day.isoformat()} {random.randint(1000,9999)}\n")

        ts = rand_ts(day)
        env = {**os.environ,
               "GIT_AUTHOR_DATE": ts,
               "GIT_COMMITTER_DATE": ts}

        git("add", ".")
        git("commit", "-m", f"chore(auto-log): {ts}", env=env)

    day += timedelta(days=1)

print("✅ Commits generated – push with:\n   git push origin main")
