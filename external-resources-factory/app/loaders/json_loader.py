import json
from dataclasses import dataclass
from typing import Any

from app.loaders.data_loader import DataLoader


@dataclass
class JsonDataLoader(DataLoader):
    """ Takes path as an argument, that will be used to establish connection with file"""
    path: str

    def load(self) -> list[dict[str, Any]]:
        """ Returns data using json.load function. It expects that structure of json will be list of objects"""
        with open(self.path, 'r') as f:
            return json.load(f)
