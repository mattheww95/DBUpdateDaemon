"""
A dataclass to hold the database config files for the daemon

2022-06-07: Matthew Wells
"""
from dataclasses import dataclass
import os

@dataclass
class DBConfig:
    DBStorage: os.path = "data/" # temp path to hold for testing
    RecursePath: os.path = "test"