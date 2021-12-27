"""
pyifc.compress
--------------

Compress and pack .ifc files.
"""
from pyifc.compress._compress import compress
from pyifc.compress._exceptions import FileExtensionError
from pyifc.compress._pack import compress_and_tar, compress_and_zip
from pyifc.compress._validators import existence_validator, extension_validator

__all__ = [
    "compress",
    "compress_and_tar",
    "compress_and_zip",
    "FileExtensionError",
    "extension_validator",
    "existence_validator",
]
