from dataclasses import dataclass
from typing import Any

from app.loaders.data_loader import DataLoader
from app.loaders.xlsx_loader import XlsxDataLoader


@dataclass
class XlsxStrDataLoaderAdapter(DataLoader):
    """
    Class XlsxStrDataLoaderAdapter

    Adapter class for loading data from a Xlsx file as a list of dictionaries with string values.

    Attributes:
        path (str): The path to the Xlsx file.
        adaptee (DataLoader): The adaptee object used for loading the data. Defaults to XlsxDataLoader.

    Methods:
        load() -> list[dict[str, Any]]:
            Load the data from the Xlsx file and return it as a list of dictionaries with string values.

    """
    path: str
    adaptee: DataLoader = XlsxDataLoader

    def load(self) -> list[dict[str, Any]]:
        """
        Loads data from a file using the adaptee method and returns it as a list of dictionaries.

        Returns:
            A list of dictionaries where each dictionary represents an object in the loaded data.

        Example Usage:
            data = obj.load()
        """
        data = self.adaptee(self.path).load()
        return [dict([(k, str(v)) for k, v in obj.items()]) for obj in data]
