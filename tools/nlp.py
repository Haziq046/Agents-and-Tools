"""
Light-weight NLP helpers – NO heavy ML deps,
kept deliberately simple for demo purposes.
"""
import re
from textwrap import shorten


def summarize_text(text: str, width: int = 100) -> str:
    """Return the first *width* chars + ellipsis."""
    return shorten(text.replace("\n", " "), width=width, placeholder="…")


def analyze_sentiment(text: str) -> str:
    """Super-naïve rule-based sentiment."""
    lowered = text.lower()
    positive_keywords = {"good", "great", "awesome", "love", "amazing", "fantastic"}
    negative_keywords = {"bad", "terrible", "hate", "awful", "worst"}

    pos = any(word in lowered for word in positive_keywords)
    neg = any(word in lowered for word in negative_keywords)

    if pos and not neg:
        return "Positive 😀"
    if neg and not pos:
        return "Negative 😞"
    return "Neutral 😐"
