"""
pyifc.compress
--------------

Compress and pack .ifc files.
"""
from pyifc.compress._compress import compress
from pyifc.compress._pack import compress_and_tar, compress_and_zip

__all__ = ["compress", "compress_and_tar", "compress_and_zip"]
