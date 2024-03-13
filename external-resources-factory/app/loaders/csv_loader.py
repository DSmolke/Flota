import csv
from dataclasses import dataclass
from typing import Any
from app.loaders.data_loader import DataLoader


@dataclass
class CsvDataLoader(DataLoader):
    """
    Takes path as an argument, that will be used to establish connection with file
    sep has default value of ',' but can be change for any separator that is currently used in source file
    """
    path: str
    sep: str = ','

    def load(self) -> list[dict[str, Any]]:
        """ Returns data using json.load function. It expects that structure of json will be list of objects"""
        rows = []
        with open(self.path, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)

        return [dict(zip(header, row)) for row in rows]
