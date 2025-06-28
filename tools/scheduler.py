"""
Tiny cron-like helper. In real life you’d use APScheduler / Celery,
but this shows how you might grow utilities in the toolkit.
"""
from datetime import datetime, timedelta
from typing import Callable, List


class SimpleScheduler:
    def __init__(self) -> None:
        self._events: List[tuple[datetime, Callable[[], None]]] = []

    def schedule(self, delay: timedelta, func: Callable[[], None]) -> None:
        self._events.append((datetime.utcnow() + delay, func))

    def run_pending(self) -> None:
        now = datetime.utcnow()
        for event_time, func in list(self._events):
            if event_time <= now:
                func()
                self._events.remove((event_time, func))
