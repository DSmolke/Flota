import jsonlines
from dataclasses import dataclass
from typing import Any

from app.loaders.data_loader import DataLoader

@dataclass
class JsonlDataLoader(DataLoader):
    """ Takes path as an argument, that will be used to establish connection with file"""
    path: str

    def load(self) -> list[dict[str, Any]]:
        """ Returns data using jsonlines.open() function. It expects classic jsonl object"""
        with jsonlines.open(self.path, 'r') as f:
            return [obj for obj in f]
