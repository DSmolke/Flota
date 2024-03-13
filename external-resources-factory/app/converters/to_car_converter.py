from typing import Self

from app.converters.converter import Converter
from app.models.car import CarInterface, Car


class ToCarsConverter(Converter):
    def convert(self, data: list[dict[str, CarInterface]]) -> list[CarInterface]:
        """
        :param data: list of dict representations of car
        :return: list of Cars
        """
        return [Car.from_dict(element) for element in data]

    def __eq__(self, other: Self) -> bool:
        return type(self) == type(other)
