# -*- coding: utf-8 -*-
"""This module that the setting instance has all the needed properties.

Created on: 22/6/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import os
from pathlib import Path
from pydantic import BaseSettings
from sparkifydb.core.settings import settings, Settings


def test_setting_is_subclass_of_base_settings():
    """Test that Settings class inherits from BaseSettings."""
    assert issubclass(Settings, BaseSettings)


def test_version_proyect_path():
    """Test the project path."""
    assert settings.PROJECT_PATH == Path(__file__).parents[2]


def test_version_configurations_path():
    """Test the configuration path."""
    assert settings.CONFIG_PATH == settings.PROJECT_PATH / "config"


def test_configurations_path_exists():
    """Test if configuration path exists."""
    assert os.path.exists(
        settings.PROJECT_PATH / "config"
    )


def test_db_credentials_have_valid_values():
    """Test if the databse credential were correctly loaded from .env file."""
    assert (
            isinstance(settings.DB_USER_NAME, str)
            and isinstance(settings.DB_PASS, str)
    )

