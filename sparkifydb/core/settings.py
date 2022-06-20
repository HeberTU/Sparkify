# -*- coding: utf-8 -*-
"""Configuration script.

Created on: 20/6/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from typing import Optional
from pydantic import BaseSettings, Field

# TODO heber.trujilloglovoapp.com - 20/6/22: use inheritance to inyect all
#  BaseSettings functionalities into Settinggs class.
#  Check this article: https://ellibrodepython.com/herencia-en-python
class Settings():
    """Setting management system for to dynamically load env variables."""

    class Config:
        """Loads the dotenv file."""

        # TODO heber.trujilloglovoapp.com - 20/6/22: Fix (repair) env_file
        #  variable by:
        #   1. annotate it as string. Hint -> a: int = 1, variable a is an int
        #   2. Assign it the name of the file wehre environmental variables are
        #   stored

    # TODO heber.trujilloglovoapp.com - 20/6/22: Fix (repair) PROJECT_PATH
    #  variable by:
    #   1. annotate it as the a a class that resembles a Directory.
    #   Hint -> pydantic types module has a directory path class check the
    #   docs https://pydantic-docs.helpmanual.io/usage/types/#typeddict
    #   2. Assign it the  project directory DYNAMICALLY (not hardcoded)
    #   it should be something like "/Users/montse/projects/Sparkify"
    #   Hint -> use the an instance of Path class and the __file__ variable
    #   for Path: try init Path class passing __file__ and check parents method
    #   for __file__ check: https://note.nkmk.me/en/python-script-file-path/

    PROJECT_PATH = None

    # TODO heber.trujilloglovoapp.com - 20/6/22: Fix (repair) PROJECT_PATH
    #  variable by:
    #   1. use same annotation as for PROJECT_PATH variable
    #   2. use the / of Path class to extend the PROJECT_PATH
    #   to "/Users/montse/projects/Sparkify/config/"
    CONFIG_PATH = PROJECT_PATH

    # TODO heber.trujilloglovoapp.com - 20/6/22: Check if the CONFIG_PATH
    #  directory exists and if note creat it hints:
    #  1. look for os.path.exists documentation
    #  2. look for os.makedirs documentation
    if not False:
        pass # change pass to something like os.makedirst(blablabla)

    # TODO heber.trujilloglovoapp.com - 20/6/22: the value for the following
    #  variables should come from the .env file located at the project root.
    DB_USER_NAME: Optional[str] = Field(None)
    DB_PASS: Optional[str] = Field(None)



# TODO heber.trujilloglovoapp.com - 20/6/22: create an instance of Settings
#  class and nameit settings (first letter lower)
