# -*- coding: utf-8 -*-
"""This module contains object representing business logic.

Created on: 29/6/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# TODO heber.trujilloglovoapp.com - 29/6/22: Import dataclass function from
#  dataclasses module.

# TODO heber.trujilloglovoapp.com - 29/6/22: Implement the following classes as
#  dataclasses, note that they will be used to represent the SQL tables:
#  1. User
#  2. Artist
#  3. Song
#  4. Time
#  hints:
#  a) Dataclass attrbutes represent columns
#  b) Table definitions can be found in "~/Aparkify/sql_queries.py", for
#   example, user table is defined in line 26.
#   c) some SQL-Python types equivalences:
#       - varchar -> str
#       - timestamp -> date from datetime module
#   c) If the SQL column is NOT declared as Nullable, you can use the Optional
#    python annotation
#   d) The following columns DON'T have to be an attribute on any dataclass:
#       - user_id
#       - song_id
#       - artist_id


# ---- EXAMPLE ----
# @dataclass(frozen=True) <--- /!\ IMPORTANT /!\ Investigate why frozen=True.
# class Carta:  <------------- The class name most be Carta, no carta nor CARTA
#   palo: str   <------------- palo attribute represents: "corazones", etc
#   numero: int <------------- numero attribute represent: 1, 2, ...


# I have prepared a mini-template for you to have a docstring
# reference: """Sparkify user representation"""
class User:
    """Sparkify user representation."""

    pass
