# -*- coding: utf-8 -*-
"""This module checks if the package version has been change for a new release.

Created on: 18/6/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from sparkifydb import __version__


def test_version():
    """Test package version for new release."""
    assert __version__ == "0.2.0"
