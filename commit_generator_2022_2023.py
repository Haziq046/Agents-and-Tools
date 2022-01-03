#!/usr/bin/env python
"""
Natural-looking back-dated commits for 2022-2023
───────────────────────────────────────────────
• Average gap ≈ 3 days (but varies 1-6)
• 1-4 commits on a commit-day (biased toward 1-2)
• ~10 % of weeks completely silent (vacations)
"""

from __future__ import annotations
import os, random, subprocess
from datetime import date, datetime, timedelta

# ─── CONFIG ───────────────────────────────────────────────────────────────────
REPO_PATH   = os.path.abspath(os.path.dirname(__file__))
START_DATE  = date(2022, 1, 1)
END_DATE    = date(2023, 12, 31)

GAP_LAMBDA  = 3.0               # average days between commit-batches
WEEK_OFF_PROB = 0.10            # 10 % chance to mute a full week
COMMITS_PER_DAY_WEIGHTS = {1: 0.5, 2: 0.3, 3: 0.15, 4: 0.05}

WORK_HOURS = range(9, 18)       # office-hour timestamps
TARGET_FILE = os.path.join(REPO_PATH, "agents", "base.py")
# ──────────────────────────────────────────────────────────────────────────────


def git(*args: str, env: dict | None = None) -> None:
    subprocess.run(["git", *args], cwd=REPO_PATH, check=True, env=env)


def random_gap() -> int:
    """Return a gap length ≥1 drawn from a geometric-like distribution."""
    # P(gap=k) ≈ exp(-k/λ) ; but simple while loop is fine here
    while True:
        k = random.randint(1, 6)          # cap 6 to avoid huge holes
        if random.random() < pow(2.71828, -k / GAP_LAMBDA):
            return k


def rand_timestamp(d: date) -> str:
    dt = datetime(
        d.year, d.month, d.day,
        random.choice(WORK_HOURS),
        random.randint(0, 59),
        random.randint(0, 59),
    )
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def weighted_choice(table: dict[int, float]) -> int:
    """Return key chosen by its probability weight."""
    r = random.random()
    cum = 0.0
    for k, w in table.items():
        cum += w
        if r <= cum:
            return k
    return k  # fallback


def main() -> None:
    os.chdir(REPO_PATH)
    print(f"Repo ➜ {REPO_PATH}")

    # pre-select “vacation” weeks
    vacation_weeks = {w for w in range(1, 54) if random.random() < WEEK_OFF_PROB}
    print("📆 Silent weeks (ISO):", sorted(vacation_weeks))

    day: date = START_DATE
    while day <= END_DATE:
        iso = day.isocalendar()
        if iso.week in vacation_weeks or iso.weekday >= 6:
            day += timedelta(days=1)
            continue

        # decide how many commits today
        commits_today = weighted_choice(COMMITS_PER_DAY_WEIGHTS)

        for _ in range(commits_today):
            # trivial edit so commit isn’t empty
            with open(TARGET_FILE, "a", encoding="utf-8") as f:
                f.write(f"# auto-log {day.isoformat()} {random.randint(1000,9999)}\n")

            ts = rand_timestamp(day)
            env = {**os.environ,
                   "GIT_AUTHOR_DATE": ts,
                   "GIT_COMMITTER_DATE": ts}

            git("add", ".")
            git("commit", "-m", f"chore(auto-log): {ts}", env=env)

        # jump ahead by a *random* gap
        day += timedelta(days=random_gap())

    print("✅ Commits generated — push with:\n   git push origin main")


if __name__ == "__main__":
    main()
