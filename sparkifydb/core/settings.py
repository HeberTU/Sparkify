# -*- coding: utf-8 -*-
"""Configuration script.

Created on: 20/6/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import os
from pathlib import Path, PosixPath
from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Setting management system for to dynamically load env variables."""
    # environment specific variables do not need the Field class

    DB_USER_NAME: Optional[str] = Field(None)
    DB_PASS: Optional[str] = Field(None)

    class Config:
        """Loads the dotenv file."""
        env_file: str = ".env"

    PROJECT_PATH: PosixPath = Path(__file__).parents[2]

    CONFIG_PATH:  PosixPath = PROJECT_PATH / 'config'

    if not os.path.exists(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)


settings = Settings()
