"""Python package template."""

from __future__ import annotations

from ._version import __version__, __version_tuple__
from .core import add, div, mul, sub

__all__ = ["__version__", "__version_tuple__", "add", "div", "mul", "sub"]
