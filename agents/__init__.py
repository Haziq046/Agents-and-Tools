"""
Agents-and-Tools – agents package
Automatically exposes concrete agent classes at package level
so you can do:

>>> from agents import ChatAgent
"""
from .chat import ChatAgent  # noqa: F401
