# -*- coding: utf-8 -*-
"""Business logic unit tests.

Created on: 29/6/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from dataclasses import is_dataclass

import pytest
from _pytest.fixtures import FixtureFunction


@pytest.mark.unit
def test_all_domain_classes_are_implemented(
    get_implemented_domain_objects: FixtureFunction,
    get_domain_objects: FixtureFunction,
) -> None:
    """Test if all the needed classes are implemented."""
    domain_objects = get_domain_objects
    implemented_domain_dict_objects = get_implemented_domain_objects

    implemented_object_names = set(implemented_domain_dict_objects.keys())

    missing_implementations = domain_objects - implemented_object_names

    msg = "The following classes are not implemented in model "
    msg += f"module: {missing_implementations}"

    assert len(missing_implementations) == 0, msg


@pytest.mark.unit
def test_all_domain_classes_are_dataclasses(
    get_implemented_domain_objects: FixtureFunction,
    table_definitions: FixtureFunction,
) -> None:
    """Test if all the needed classes are implemented as dataclasses."""
    implemented_domain_dict_objects = get_implemented_domain_objects
    table_definitions_dict = table_definitions

    implemented_domain_dict_objects = {
        k: v
        for k, v in implemented_domain_dict_objects.items()
        if k in table_definitions_dict.keys()
    }

    for name, obj in implemented_domain_dict_objects.items():
        msg = f"Object {name} has to be implemented as a dataclass."
        assert is_dataclass(obj), msg


@pytest.mark.unit
def test_all_and_only_needed_domain_dataclasse_attrbutes_are_implemented(
    get_implemented_domain_objects: FixtureFunction,
    table_definitions: FixtureFunction,
) -> None:
    """Test if all the needed dataclasses have the correct columns(attr)."""
    implemented_domain_dict_objects = get_implemented_domain_objects
    table_definitions_dict = table_definitions

    for name, obj in implemented_domain_dict_objects.items():
        domain_columns = table_definitions_dict[name]
        implemented_columns = set(obj.__annotations__.keys())

        missing_columns = domain_columns - implemented_columns

        msg = f"The following columns are not implemented for {name}"
        msg += f"class: {missing_columns}"

        assert len(missing_columns) == 0, msg

        extra_columns = implemented_columns - domain_columns

        msg = f"The following columns should NOT be implemented in {name}"
        msg += f"class: {extra_columns}"

        assert len(extra_columns) == 0, msg
