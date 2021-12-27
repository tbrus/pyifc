"""
https://github.com/tbrus/pyifc
------------------------------

pyifc: Utilities for .ifc files

pyifc is a Python package that provides utilities for working with .ifc files.
"""

from pyifc import compress
from pyifc._version import version

__version__ = version

__all__ = ["compress"]
