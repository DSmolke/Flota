import json
import logging
from unittest import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from drivers.models import DriverModel
import logging
logging.basicConfig(level=logging.INFO)

def create_driver() -> DriverModel:
    driver = DriverModel.objects.create(
        first_name='A',
        last_name='AA',
        email='a@gmail.com',
        phone_number='111111111',
        car_registration='AAAAAAA'
    )
    return driver


def delete_all_drivers() -> None:
    DriverModel.objects.all().delete()


class TestDriverModel(TestCase):
    def test_create_one_driver(self) -> None:
        delete_all_drivers()
        driver = create_driver()
        self.assertIsNotNone(driver)
        self.assertIsNotNone(driver.id)

    def test_delete_driver(self) -> None:
        delete_all_drivers()
        driver = create_driver()
        driver.delete()
        self.assertIsNone(driver.id)


class AllDriversResourceTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_insert_and_get_all_drivers(self) -> None:
        delete_all_drivers()
        create_driver()
        response = self.client.get('/drivers/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)


class AddDriverResourceTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_insert_one_driver(self) -> None:
        delete_all_drivers()
        response = self.client.post(
            '/driver',
            json.dumps(
                {
                    "first_name": "Szymon",
                    "last_name": "Gierlach",
                    "phone_number": "570688765",
                    "email": "s.gierlachpl@gmail.com",
                    "car_registration": "DPL96RR"
                }
            ),
            content_type='application/json'
        )

        self.assertIsNotNone(response.data['id'])


class DriversResourceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        delete_all_drivers()
        self.new_driver = create_driver()

    def test_get_one_driver(self) -> None:
        response = self.client.get(f'/driver/{self.new_driver.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.new_driver.first_name)

    def test_update_driver(self) -> None:
        response = self.client.patch(
            f'/driver/{self.new_driver.id}',
            json.dumps(
                {
                    "email": "d.smolczynski@gmail.com"
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "d.smolczynski@gmail.com")

    def test_delete_driver(self) -> None:
        response = self.client.delete(
            f'/driver/{self.new_driver.id}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "message": "Driver has been deleted"
        })

    def test_delete_driver_not_found(self) -> None:
        delete_all_drivers()
        response = self.client.delete(
            f'/driver/{self.new_driver.id}'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"message": "Driver not found"})

    def test_get_one_that_not_exists(self) -> None:
        delete_all_drivers()
        response = self.client.get(f'/driver/{self.new_driver.id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
