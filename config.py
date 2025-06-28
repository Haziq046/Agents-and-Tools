"""
Centralised constants / env parsing (expand later).
"""
import os

DEBUG = bool(int(os.getenv("AGENTS_DEBUG", "0")))
