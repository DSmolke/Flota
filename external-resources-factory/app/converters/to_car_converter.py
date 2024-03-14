from typing import Self

from app.converters.converter import Converter
from app.models.car import Car
from app.models.model_interface import ModelInterface


class ToCarsConverter(Converter):
    def convert(self, data: list[dict[str, ModelInterface]]) -> list[ModelInterface]:
        """
        :param data: list of dict representations of car
        :return: list of Cars
        """
        return [Car.from_dict(element) for element in data]

    def __eq__(self, other: Self) -> bool:
        return type(self) == type(other)
