#!/usr/bin/env python
"""
Generate natural-looking back-dated commits for the last 18 months.

• Weekdays only
• 1-4 commits per day
• Random vacation week ~every 2 months
"""

from __future__ import annotations
import subprocess
import os
import random
from datetime import datetime, timedelta, date

# CONFIG ----------------------------------------------------------------------
REPO_PATH = os.path.abspath(os.path.dirname(__file__))  # repo root
START_DATE = date(2024, 1, 1)
END_DATE = date.today()
WORK_HOURS = range(9, 18)          # 09:00-17:59
COMMITS_PER_DAY = (1, 4)           # inclusive (min, max)
VACATION_CHANCE = 1 / 8            # 1 in 8 weeks off
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")
# -----------------------------------------------------------------------------

def random_dt(d: date) -> datetime:
    hr = random.choice(WORK_HOURS)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime(d.year, d.month, d.day, hr, minute, second)

def git(*args: str, env: dict | None = None) -> None:
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)

def main() -> None:
    os.chdir(REPO_PATH)
    print(f"Repo root ➜ {REPO_PATH}")

    # Determine vacation weeks up-front
    vac_weeks: set[int] = set()
    cursor = START_DATE
    while cursor <= END_DATE:
        iso_week = cursor.isocalendar().week
        if random.random() < VACATION_CHANCE:
            vac_weeks.add(iso_week)
        cursor += timedelta(weeks=1)

    print(f"Vacation weeks (ISO numbers): {sorted(vac_weeks)}")

    current = START_DATE
    while current <= END_DATE:
        weekday = current.weekday()        # 0-Mon … 6-Sun
        iso_week = current.isocalendar().week

        if weekday >= 5 or iso_week in vac_weeks:  # weekend or vacation
            current += timedelta(days=1)
            continue

        for _ in range(random.randint(*COMMITS_PER_DAY)):
            # append a tiny update so commit isn't empty
            with open(TARGET_FILE, "a", encoding="utf-8") as fh:
                fh.write(f"# auto-log {current.isoformat()} {random.randint(1000,9999)}\n")

            commit_dt = random_dt(current)
            ts = commit_dt.strftime("%Y-%m-%dT%H:%M:%S")
            env = {**os.environ,
                   "GIT_AUTHOR_DATE": ts,
                   "GIT_COMMITTER_DATE": ts}

            git("add", ".")
            git("commit", "-m", f"chore(auto-log): {ts}", env=env)

        current += timedelta(days=1)

    print("✔️  History generated – push with:\n   git push origin main")

if __name__ == "__main__":
    main()
