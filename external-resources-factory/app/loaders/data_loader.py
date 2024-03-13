from abc import abstractmethod, ABC
from typing import Any


class DataLoader(ABC):
    """ Abstract class that provides abstract method: load"""
    @abstractmethod
    def load(self) -> list[dict[str, Any]]:
        """ How loading of resource will look like """
        pass
