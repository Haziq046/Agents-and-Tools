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
