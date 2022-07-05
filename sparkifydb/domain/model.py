# -*- coding: utf-8 -*-
"""This module contains object representing business logic.

Created on: 29/6/22
@authors:
    - Heber Trujillo <heber.trj.urt@gmail.com>
    - Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True, unsafe_hash=True)
class User:
    """Sparkify user representation."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    level: Optional[str] = None

@dataclass(order=True, unsafe_hash=True)
class Artist:
    """Sparkify artist representation."""
    name: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitud: Optional[float] = None

@dataclass(order=True, unsafe_hash=True)
class Song:
    """Sparkify song representation."""
    title: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[float] = None

@dataclass(order=True, unsafe_hash=True)
class Time:
    """Sparkify time representation."""
    # start_time: datetime = field(default_factory=datetime.utcnow)
    start_time: str
    hour: Optional[int] = None
    day: Optional[int] = None
    week: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    weekday: Optional[int] = None

