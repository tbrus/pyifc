"""
pyifc.compress._compress
------------------------

Functions for compressing .ifc files.
"""

import os
from typing import Dict

import ifcopenshell
from toposort import toposort_flatten

from pyifc.compress._validators import existence_validator, extension_validator


def get_instances_and_references(file):
    """Returns dictionary of instances ids and their references from
    .ifc file.

    Args:
        file (ifcopenshell.file.file): .ifc file object returned by
            ifcopenshell.open() function.

    Returns:
        dict: dictionary of instances ids mapped to its references.
    """
    dict_ = dict()

    for instance in file:
        key = instance.id()
        # The first occurrence `references[0]` is the instance (key)
        # so choose `references[1:]`
        references = file.traverse(instance)[1:]
        value = set(ref.id() for ref in references if ref.id())
        dict_[key] = value
    return dict_


def compress(input_filepath, output_dir, output_filename):
    """Compress ifc file and return path to the compressed file.

    The core of the algorithm is toposort_flatten function which allows to
    sort topologically instances from the ifc file. Two dictionaries are used
    to store data from file: `dict_map_instance` and `dict_info_id`.

    The first step is to check if info of the instance is in `dict_info_id`.
    If so, the dictionary of mapped instances is used `dict_map_instance`.
    Instance is mapped to another instance that appeared earlier. In this way,
    the instances will not be duplicated.

    If the instance with given attrs did not appeared earlier, the instance
    and its info is added to `dict_info_id` and added to new ifc file with
    attrs obtained with `map_references_to_instances` function which
    recursively traverse attrs of the instance.

    Args:
        input_filepath (str): path to ifc file to be compressed.
        output_dir (str): path to output directory, where compressed file
            will be saved.
        output_filename (str): filename with '.ifc' extension.

    Returns:
        str: path to the compressed file.
    """

    # Validate correctness of the arguments
    extension_validator(
        filepath=input_filepath,
        extension=".ifc",
        variable="input_filepath",
    )
    extension_validator(
        filepath=output_filename,
        extension=".ifc",
        variable="output_filename",
    )
    existence_validator(input_filepath)
    existence_validator(output_dir)

    # Schema from the file should be applied to the new file to maintain
    # compatibility
    file = ifcopenshell.open(input_filepath)
    schema = file.schema
    new_file = ifcopenshell.file(schema=schema)

    dict_map_instance: Dict[
        ifcopenshell.entity_instance, ifcopenshell.entity_instance
    ] = dict()
    dict_info_id: Dict[frozenset, int] = dict()

    def map_references_to_instances(instance):
        nonlocal dict_map_instance
        nonlocal new_file
        if isinstance(instance, (list, tuple)):
            return type(instance)(map(map_references_to_instances, instance))
        elif isinstance(instance, ifcopenshell.entity_instance):
            if instance.id() == 0:
                return new_file.create_entity(instance.is_a(), instance[0])
            return dict_map_instance[instance]
        else:
            return instance

    for id in toposort_flatten(get_instances_and_references(file)):
        instance = file[id]
        info = instance.get_info(
            include_identifier=False, recursive=True, return_type=frozenset
        )

        if info in dict_info_id:
            dict_map_instance[instance] = dict_map_instance[
                file[dict_info_id[info]]
            ]

        else:
            dict_info_id[info] = id
            instance_type = instance.is_a()
            instance_attrs = map(map_references_to_instances, instance)

            dict_map_instance[instance] = new_file.create_entity(
                instance_type, *instance_attrs
            )

    output_filepath = os.path.abspath(
        os.path.join(output_dir, output_filename)
    )
    new_file.write(output_filepath)

    return os.path.abspath(output_filepath)
