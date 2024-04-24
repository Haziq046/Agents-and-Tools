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
# auto-log 2024-02-08 3286
# auto-log 2024-02-09 4479
# auto-log 2024-02-09 5134
# auto-log 2024-02-09 5341
# auto-log 2024-02-12 8709
# auto-log 2024-02-12 1661
# auto-log 2024-02-12 8830
# auto-log 2024-02-12 3897
# auto-log 2024-02-13 3804
# auto-log 2024-02-13 5934
# auto-log 2024-02-13 7432
# auto-log 2024-02-14 4826
# auto-log 2024-02-14 9487
# auto-log 2024-02-15 1648
# auto-log 2024-02-15 7292
# auto-log 2024-02-16 6013
# auto-log 2024-02-16 3254
# auto-log 2024-02-16 5238
# auto-log 2024-02-16 2098
# auto-log 2024-03-04 3916
# auto-log 2024-03-04 7628
# auto-log 2024-03-05 6838
# auto-log 2024-03-06 7895
# auto-log 2024-03-06 3434
# auto-log 2024-03-07 7369
# auto-log 2024-03-07 7954
# auto-log 2024-03-07 8025
# auto-log 2024-03-07 3019
# auto-log 2024-03-08 1998
# auto-log 2024-03-08 7953
# auto-log 2024-03-08 4788
# auto-log 2024-03-08 4078
# auto-log 2024-03-11 3662
# auto-log 2024-03-11 6820
# auto-log 2024-03-12 5081
# auto-log 2024-03-13 5729
# auto-log 2024-03-13 4717
# auto-log 2024-03-14 1873
# auto-log 2024-03-14 3541
# auto-log 2024-03-15 1473
# auto-log 2024-03-15 1232
# auto-log 2024-03-15 8527
# auto-log 2024-03-18 2547
# auto-log 2024-03-19 7879
# auto-log 2024-03-19 4766
# auto-log 2024-03-19 2728
# auto-log 2024-03-20 4734
# auto-log 2024-03-20 9855
# auto-log 2024-03-21 9742
# auto-log 2024-03-22 6020
# auto-log 2024-03-22 2618
# auto-log 2024-03-22 9239
# auto-log 2024-03-25 2460
# auto-log 2024-03-25 6268
# auto-log 2024-03-25 9060
# auto-log 2024-03-26 4474
# auto-log 2024-03-26 1898
# auto-log 2024-03-26 8185
# auto-log 2024-03-27 9461
# auto-log 2024-03-27 6609
# auto-log 2024-03-28 8398
# auto-log 2024-03-28 8625
# auto-log 2024-03-28 6371
# auto-log 2024-03-29 7188
# auto-log 2024-04-01 4809
# auto-log 2024-04-02 3163
# auto-log 2024-04-02 7935
# auto-log 2024-04-02 9405
# auto-log 2024-04-02 8724
# auto-log 2024-04-03 3795
# auto-log 2024-04-03 2112
# auto-log 2024-04-04 2361
# auto-log 2024-04-05 5872
# auto-log 2024-04-05 7274
# auto-log 2024-04-08 6102
# auto-log 2024-04-08 8833
# auto-log 2024-04-08 2403
# auto-log 2024-04-08 3916
# auto-log 2024-04-09 4577
# auto-log 2024-04-10 9355
# auto-log 2024-04-11 5968
# auto-log 2024-04-12 9020
# auto-log 2024-04-12 1163
# auto-log 2024-04-15 2040
# auto-log 2024-04-15 9912
# auto-log 2024-04-16 8984
# auto-log 2024-04-17 9145
# auto-log 2024-04-17 4681
# auto-log 2024-04-17 3600
# auto-log 2024-04-17 1596
# auto-log 2024-04-18 9117
# auto-log 2024-04-18 6347
# auto-log 2024-04-19 7474
# auto-log 2024-04-19 6449
# auto-log 2024-04-22 4285
# auto-log 2024-04-22 4289
# auto-log 2024-04-22 1923
# auto-log 2024-04-23 2981
# auto-log 2024-04-23 7846
# auto-log 2024-04-24 3243
# auto-log 2024-04-24 8464
# auto-log 2024-04-24 6453
