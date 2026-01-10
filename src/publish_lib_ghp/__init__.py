"""publish_lib_ghp - A simple Python library demonstrating how to publish packages to PyPI."""

import sys

from importlib.metadata import version

try:
    __version__ = version("publish-lib-ghp")
except Exception:
    # Fallback for development environments
    __version__ = "0.0.0-dev"

from .greeting import Greeting
from .operations import Operations