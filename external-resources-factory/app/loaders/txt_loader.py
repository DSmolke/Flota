from dataclasses import dataclass
from typing import Any
from app.loaders.data_loader import DataLoader


@dataclass
class TxtDataLoader(DataLoader):
    """ Takes path as an argument, that will be used to establish connection with file"""
    path: str
    sep: str = ','

    def load(self) -> list[dict[str, Any]]:
        """ Returns data using json.load function. It expects that structure of json will be list of objects"""
        with open(self.path, 'r') as file:
            headers = [header if '\n' not in header else header[:-1] for header in file.readline().split(',')]
            rows = [[v if '\n' not in v else v[:-1] for v in values.split(',')] for values in file.readlines()]
        return [dict(zip(headers, row)) for row in rows]
