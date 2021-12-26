"""
pyifc.compress._exceptions
--------------------

Validators used in pyifc.compress module.
"""

import os

from pyifc.compress._exceptions import FileExtensionError


def extension_validator(filepath, extension, variable):
    """Validate whether the `filepath` has correct extension or not.

    Args:
        filepath (str): path to filename to be checked.
        extension (str): extension that filename should have.
        variable (str): name of variable of filepath.

    Raises:
        FileExtensionError: if filename does not have `extension`
            extension.
    """
    if not filepath.endswith(extension):
        got_ext = filepath.rsplit(".")[-1]
        msg = (
            f"{variable} should have {extension} extension; "
            f"got .{got_ext} extension"
        )
        raise FileExtensionError(msg)


def existing_validator(path):
    """Validate whether the path exists or not.

    Args:
        path (str): path to be checked.

    Raises:
        FileNotFoundError: if path does not exist.
    """
    if not os.path.exists(path):
        msg = f"No such file or directory: {path}"
        raise FileNotFoundError(msg)
