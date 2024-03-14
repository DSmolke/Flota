from dataclasses import dataclass
from typing import Any

from easyvalid_data_validator.constraints import Constraint

from app.factories.data_factory import DataFactory
from app.converters.to_liability_converter import ToLiabilityConverter
from app.loaders.sqlite_loader import Sqlite3DataLoader
from app.validators.json_dict_validator import JsonDictValidator


@dataclass
class FromSqlite3ToLiabilitiesWithExpectedConstraintsDataFactory(DataFactory):
    """
    path: path of .db file that has to load cars information

    constraints: dict that keys are names that will be validated and values are dict that has
        easyvalid_data_validator.constraints.Constraint objects as key and constraint (for example regex).
    Example of constraints dict:
    constraints = {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}

    query: sqlite3 dialect friendly query, that specifies what car data should be obtained
    keys: list of column names
    """
    path: str
    constraints: dict[str, dict[Constraint, Any]]
    query: str
    keys: list[str]

    def create_data_loader(self):
        """ Creates Sqltie3DataLoader using self.path, self.query, self.keys """
        return Sqlite3DataLoader(self.path, self.query, self.keys)

    def create_validator(self):
        """ Creates JsonDictValidator using self. constraints """
        return JsonDictValidator(self.constraints)

    def create_converter(self):
        """ Creates ToCarsConverter """
        return ToLiabilityConverter()
