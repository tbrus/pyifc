"""
pyifc.compress._validators
--------------------------

Validators used in pyifc.compress module.
"""

import os

from pyifc.compress._exceptions import FileExtensionError


def extension_validator(filepath, extension, variable):
    """Validate whether the `filepath` has correct extension.

    Args:
        filepath (str): path to file to be checked.
        extension (str): extension that file should have.
        variable (str): name of variable of `filepath`.

    Raises:
        FileExtensionError: if filen does not have `extension` extension.
    """
    if not filepath.endswith(extension):
        got_ext = filepath.rsplit(".")[-1]
        msg = (
            f"{variable} should have {extension} extension; "
            f"got .{got_ext} extension"
        )
        raise FileExtensionError(msg)


def existence_validator(path):
    """Validate whether the `path` exists.

    Args:
        path (str): path to be checked.

    Raises:
        FileNotFoundError: if `path` does not exist.
    """
    abspath = os.path.abspath(path)
    if not os.path.exists(abspath):
        msg = f"No such file or directory: {abspath}"
        raise FileNotFoundError(msg)
