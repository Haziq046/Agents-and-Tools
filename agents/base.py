from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Abstract base class for every agent in the framework.

    Sub-classes MUST override :meth:`act`.
    """

    def __init__(self, name: str, metadata: Dict[str, Any] | None = None) -> None:
        self.name = name
        self.metadata = metadata or {}
        logger.debug("Created agent '%s' with metadata=%s", self.name, self.metadata)

    @abstractmethod
    def act(self, input_data: Any) -> Any:  # pragma: no cover
        """Perform an action and return a result."""
        raise NotImplementedError
# auto-log 2024-01-01 9426
# auto-log 2024-01-01 1117
# auto-log 2024-01-01 7463
# auto-log 2024-01-01 4763
# auto-log 2024-01-02 5093
# auto-log 2024-01-03 6876
# auto-log 2024-01-03 3676
# auto-log 2024-01-04 1515
# auto-log 2024-01-04 6764
# auto-log 2024-01-05 6399
# auto-log 2024-01-05 6379
# auto-log 2024-01-08 4977
# auto-log 2024-01-08 4384
# auto-log 2024-01-08 7345
# auto-log 2024-01-08 2792
# auto-log 2024-01-09 2454
# auto-log 2024-01-10 8402
# auto-log 2024-01-10 5261
# auto-log 2024-01-11 9127
# auto-log 2024-01-11 7367
# auto-log 2024-01-11 1894
# auto-log 2024-01-12 9981
# auto-log 2024-01-12 4396
# auto-log 2024-01-12 1253
# auto-log 2024-01-15 4179
# auto-log 2024-01-15 2809
# auto-log 2024-01-15 8118
# auto-log 2024-01-15 7978
# auto-log 2024-01-16 8397
# auto-log 2024-01-16 9333
# auto-log 2024-01-16 8661
# auto-log 2024-01-17 4560
# auto-log 2024-01-17 4041
# auto-log 2024-01-17 6909
# auto-log 2024-01-18 1680
# auto-log 2024-01-19 9464
# auto-log 2024-01-22 1298
# auto-log 2024-01-22 3516
# auto-log 2024-01-23 3326
# auto-log 2024-01-24 4916
# auto-log 2024-01-25 9019
# auto-log 2024-01-25 8444
# auto-log 2024-01-26 6221
# auto-log 2024-01-26 1499
# auto-log 2024-01-26 4555
# auto-log 2024-01-29 8663
# auto-log 2024-01-30 7669
# auto-log 2024-01-30 2922
# auto-log 2024-01-30 3282
# auto-log 2024-01-31 1882
# auto-log 2024-01-31 2634
# auto-log 2024-01-31 1621
# auto-log 2024-01-31 1305
# auto-log 2024-02-01 7087
# auto-log 2024-02-02 4762
# auto-log 2024-02-05 5196
# auto-log 2024-02-05 6547
# auto-log 2024-02-06 3203
# auto-log 2024-02-06 6917
# auto-log 2024-02-06 1571
# auto-log 2024-02-06 3798
# auto-log 2024-02-07 9933
# auto-log 2024-02-07 3351
# auto-log 2024-02-08 6451
# auto-log 2024-02-08 2327
