#!/usr/bin/env python
"""
Generate natural commits for 2024-01-01 → 2025-06-28 with many blank days.
"""

from __future__ import annotations
import os, random, subprocess
from datetime import date, datetime, timedelta

# ───────────────────────────────── CONFIG ────────────────────────────────────
REPO_PATH   = os.path.abspath(os.path.dirname(__file__))   # repo root
START_DATE  = date(2024, 1, 1)
END_DATE    = date(2025, 6, 28)

# vacation blocks (full silence)
VACATION_BLOCKS = random.randint(3, 6)         # how many gaps
VAC_MIN, VAC_MAX = 5, 12                       # days per gap

# probability that a *whole ISO week* is silent
SILENT_WEEK_PROB = 0.20            # 20 %

# probability an *individual weekday* fires (outside vacations)
DAY_FIRE_PROB = 0.40               # 40 %

# commits/day distribution (sum of weights = 1.0)
COMMITS_PMF = {1: 0.50, 2: 0.30, 3: 0.15, 4: 0.05}

WORK_HOURS = range(9, 22)          # 09 h – 21 h
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")
# ─────────────────────────────────────────────────────────────────────────────


# ----------------  Helpers  ----------------
def git(*args: str, env: dict | None = None):
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)

def rand_ts(d: date) -> str:
    dt = datetime(
        d.year, d.month, d.day,
        random.choice(WORK_HOURS),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return dt.isoformat(timespec="seconds")

def weighted_choice(table: dict[int, float]) -> int:
    r, acc = random.random(), 0.0
    for k, w in table.items():
        acc += w
        if r <= acc:
            return k
    return k  # fallback


# ----------------  Build vacation calendar  ----------------
vacation_days: set[date] = set()

# random long gaps
cursor = START_DATE
total_days = (END_DATE - START_DATE).days
for _ in range(VACATION_BLOCKS):
    gap_start = cursor + timedelta(days=random.randint(0, total_days))
    gap_len   = random.randint(VAC_MIN, VAC_MAX)
    for i in range(gap_len):
        vacation_days.add(gap_start + timedelta(days=i))

# random silent ISO weeks
vac_silent_weeks = {
    w for w in range(1, 54) if random.random() < SILENT_WEEK_PROB
}

# ----------------  Main loop  ----------------
day = START_DATE
print(f"Repo ➜ {REPO_PATH}")
print(f"Long vacation gaps: {VACATION_BLOCKS} (each {VAC_MIN}-{VAC_MAX} days)")
print(f"Silent ISO weeks:   {sorted(vac_silent_weeks)}")

os.chdir(REPO_PATH)

while day <= END_DATE:
    iso = day.isocalendar()

    if (
        day in vacation_days                # inside a long gap
        or iso.week in vac_silent_weeks     # whole week muted
        or iso.weekday >= 6                 # weekend
        or random.random() > DAY_FIRE_PROB  # skipped weekday
    ):
        day += timedelta(days=1)
        continue

    commits_today = weighted_choice(COMMITS_PMF)

    for _ in range(commits_today):
        # non-empty diff
        with open(TARGET_FILE, "a", encoding="utf-8") as fh:
            fh.write(f"# auto-note {day.isoformat()} {random.randint(1000,9999)}\n")

        ts = rand_ts(day)
        env = {**os.environ,
               "GIT_AUTHOR_DATE": ts,
               "GIT_COMMITTER_DATE": ts}

        git("add", ".")
        git("commit", "-m", f"chore(auto-note): {ts}", env=env)

    day += timedelta(days=1)

print("✅ Done — push with  ➜  git push origin main")
