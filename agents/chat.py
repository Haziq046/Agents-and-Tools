from __future__ import annotations
import logging
from .base import BaseAgent
from tools import nlp

logger = logging.getLogger(__name__)


class ChatAgent(BaseAgent):
    """
    A trivial chat-echo agent that showcases how an agent
    can orchestrate a pipeline of *tools*.
    """

    def act(self, input_data: str) -> str:
        logger.info("ChatAgent '%s' received input: %s", self.name, input_data)
        sentiment = nlp.analyze_sentiment(input_data)
        summary = nlp.summarize_text(input_data)

        response = (
            f"[{self.name}] Sentiment={sentiment} | "
            f"Summary ➜ {summary}"
        )
        logger.debug("ChatAgent response: %s", response)
        return response
