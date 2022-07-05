# -*- coding: utf-8 -*-
"""This module contains the database connection abstractions.

Created on: 05/07/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from enum import Enum, auto

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

# TODO heber.trujilloglovoapp.com - 5/7/22: use Python Enum to enumerate
#  the available engine, available options should be
#  1. POSTGRESS
#  2. IN_MEMORY_SQLITE


class EngineType(Enum):
    """Availables database engines."""

    pass


# TODO heber.trujilloglovoapp.com - 5/7/22:
def get_engine(engine_type: EngineType) -> Engine:
    """Generate the URL database and use it to create an engine.

    Args:
        engine_type: Database engine type.

    Returns:
        engine database engine.
    """
    # Create the url depending on the engine_type. If possible try to
    # avoid if else
    url = ""

    engine = None

    return engine


# TODO heber.trujilloglovoapp.com - 5/7/22: use the sessionmaker to
#  use the sessinmaker arguments os that the created Session follows the next
#  constrains:
#  1. Avoid autocommit (False) so the user is resposable to commite changes
#  into de database.
#  2. Do not expire the session after commit.
def get_db_session_type(engine_type: EngineType) -> Session:
    """Generate a Session class bound to the given engine type.

    Args:
        engine_type: Database engine type.

    Returns:
        Scoped database session.
    """
    engine = get_engine(engine_type)
    return None
