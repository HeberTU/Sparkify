# -*- coding: utf-8 -*-
"""Test fixtures.

Created on: 29/6/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import inspect
from typing import Any, Dict, Set

import pytest

import sparkifydb.domain.model as model


@pytest.fixture(scope="session")
def get_implemented_domain_objects() -> Dict[str, Any]:
    """Create one Batch and OrderLine.

    Returns:
        module_classes: class name - class dict.
    """
    module_classes = {
        name: obj
        for name, obj in inspect.getmembers(model)
        if inspect.isclass(obj)
    }

    return module_classes


@pytest.fixture(scope="session")
def get_domain_objects() -> Set[str]:
    """Domain model."""
    return set(["User", "Artist", "Song", "Time"])


@pytest.fixture(scope="session")
def table_definitions() -> Dict[str, Set[str]]:
    """Domain model attribute's definitions."""
    return {
        "User": set(["first_name", "last_name", "gender", "level"]),
        "Artist": set(["name", "location", "latitude", "longitud"]),
        "Song": set(["title", "year", "duration"]),
        "Time": set(
            ["start_time", "hour", "day", "week", "month", "year", "weekday"]
        ),
    }
