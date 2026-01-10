"""publish_lib_ghp - A simple Python library demonstrating how to publish packages to PyPI."""

import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

try:
    __version__ = version("publish-lib-ghp")
except Exception:
    # Fallback for development environments
    __version__ = "0.0.0-dev"

__author__ = "Gabriel Henrique Pascon"
__email__ = "gh.pascon@gmail.com"

from .greeting import Greeting

__all__ = ["Greeting", "__version__"]