from dataclasses import dataclass
from typing import Any
from openpyxl import load_workbook

from app.loaders.data_loader import DataLoader

@dataclass
class XlsxDataLoader(DataLoader):
    """ Takes path as an argument, that will be used to establish connection with file"""
    path: str

    def load(self) -> list[dict[str, Any]]:
        """ Returns data using jsonlines.open() function. It expects classic jsonl object"""
        wb = load_workbook(self.path)
        ws = wb.active
        values = ws.values
        headers = [header for header in next(values)]
        rows = [row for row in values]
        return [dict(zip(headers, row)) for row in rows]



