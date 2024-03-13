import sqlite3
from dataclasses import dataclass
from pathlib import Path
from sqlite3 import OperationalError
from typing import Any

from app.loaders.data_loader import DataLoader


@dataclass
class Sqlite3DataLoader(DataLoader):
    """
    Takes path as an argument, that will be used to establish connection with file.
    Takes sql select expression
    Takes list of strings that are desired keys for objects that will be later on converted
    """
    path: str
    query: str
    keys: list[str]

    def load(self) -> list[dict[str, Any]]:
        """
        Returns data using sqlite3.connect function. Iterator that points at tuples that are records in the table
        is expected to provide values for dicts that will be returned. Keys for this dicts are
        obtained during initialization of a loader
        """
        if not isinstance(self.query, str):
            raise TypeError('Provided argument suppose to be sql expression')

        if not Path(self.path).is_file():
            raise OperationalError('Database does not exist')

        with sqlite3.connect(self.path) as conn:
            curr = conn.cursor()
            curr.execute(self.query)

            return [dict(zip(self.keys, row)) for row in curr]
