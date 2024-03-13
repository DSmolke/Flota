from datetime import date

from app.processors.data_processor import DataProcesor
from app.models.car import Car


# class TestDataProcessor:
#     def test_process(self, cars_sql_factory) -> None:
#         processor = DataProcesor(cars_sql_factory)
#         assert processor.process()[0] == Car(
#             id=1,
#             registration_number='DB59123',
#             first_registration_date=date(2012, 3, 15),
#             vin="1234567890QWERTYU",
#             brand='BMW',
#             model='SERIES 3')
