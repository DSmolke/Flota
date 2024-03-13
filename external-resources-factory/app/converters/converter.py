from abc import ABC, abstractmethod
from typing import Any


class Converter(ABC):
    """
    Used in Processor, provides abstractions for other converters
    """

    @abstractmethod
    def convert(self, data: list[dict[str, Any]]) -> Any:
        """
        How data will be converted?
        :param data: list of dict representations of entities
        :return: list of entities
        """
        pass
