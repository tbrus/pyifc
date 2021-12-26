"""
pyifc.compress._pack
--------------------

Functions for packing .ifc files.
"""
import os
import pathlib
import tarfile
from zipfile import ZipFile

from pyifc._utils import timeit
from pyifc.compress._compress import compress
from pyifc.compress._validators import existing_validator, extension_validator


def _common(input_filepath, output_dir, output_filename, ext):
    """Common tasks to be performed before compressing and archiving.

    Tasks include:
    - validation of extensions of given arguments
    - validation of paths
    - creation of new paths and filenames

    Args:
        input_filepath (str): path to the ifc file to be compressed and
            archived.
        output_dir (str): path to output directory, where archive will be
            saved.
        output_filename (str): filename with `ext` extension.
        ext (str): extension that filename should have.

    Returns:
        tuple[str, str]: tuple of path to the compressed file and path to the
            archive.
    """
    extension_validator(
        filepath=output_filename,
        extension=ext,
        variable="output_filename",
    )

    input_filename = pathlib.PurePath(input_filepath).name
    extension_validator(
        filepath=input_filepath, extension=".ifc", variable="input_filepath"
    )

    existing_validator(input_filepath)
    existing_validator(output_dir)

    compressed_filename = (
        os.path.join(input_filename.rstrip(".ifc")) + "_compressed.ifc"
    )
    compressed_filepath = compress(
        input_filepath, output_dir, compressed_filename
    )
    output_filepath = os.path.join(output_dir, output_filename)

    return compressed_filepath, output_filepath


@timeit
def compress_and_tar(input_filepath, output_dir, output_filename):
    """Compress and write file to .tar.gz. archive.

    Args:
        input_filepath (str): path to the ifc file to be compressed and
            archived.
        output_dir (str): path to the output directory, where archive will
            be saved.
        output_filename (str): filename with '.tar.gz' extension.

    Returns:
        str: path to the archived file.
    """
    compressed_filepath, output_filepath = _common(
        input_filepath=input_filepath,
        output_dir=output_dir,
        output_filename=output_filename,
        ext=".tar.gz",
    )
    with tarfile.open(output_filepath, "w:gz") as tar:
        tar.add(compressed_filepath)
        print(
            f"Successfully compressed and archived "
            f"{os.path.abspath(input_filepath)} to "
            f"{os.path.abspath(output_filepath)}"
        )
    os.remove(compressed_filepath)
    return os.path.abspath(output_filepath)


@timeit
def compress_and_zip(input_filepath, output_dir, output_filename):
    """Compress and write file to .zip archive.

    Args:
        input_filepath (str): path to the ifc file to be compressed and
            archived.
        output_dir (str): path to the output directory, where archive will
            be saved.
        output_filename (str): filename with '.zip' extension.

    Returns:
        str: path to the archived file.
    """
    compressed_filepath, output_filepath = _common(
        input_filepath=input_filepath,
        output_dir=output_dir,
        output_filename=output_filename,
        ext=".zip",
    )
    with ZipFile(output_filepath, "w") as zip_file:
        zip_file.write(compressed_filepath)
        print(
            f"Successfully compressed and archived "
            f"{os.path.abspath(input_filepath)} to "
            f"{os.path.abspath(output_filepath)}"
        )
    os.remove(compressed_filepath)
    return os.path.abspath(output_filepath)
