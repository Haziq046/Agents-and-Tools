"""
CLI entry-point demo.

$ python app.py "Today is an awesome day!"
"""
import sys
import logging
from agents import ChatAgent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)

def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python app.py <text>")

    text = " ".join(sys.argv[1:])
    agent = ChatAgent("HelperBot")
    print(agent.act(text))


if __name__ == "__main__":
    main()
