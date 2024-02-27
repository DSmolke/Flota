from dataclasses import dataclass
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from app.service.models import CarDetails
from app.service.page_utils import VehicleHistoryInformation


@dataclass(frozen=True)
class CepikSevice:
    """
        Class representing a Cepik service for retrieving car reports.

        Args:
            driver (selenium.webdriver.Chrome): Selenium Chrome driver.
            car_details (CarDetails): Car details including registration number, VIN, and first registration date.
            vehicle_information (List[VehicleHistoryInformation], optional): List of information to retrieve from the car report. Defaults to [VehicleHistoryInformation.MOT_STATUS, Vehicle
    *HistoryInformation.INSURANCE_STATUS].
            url (str, optional): URL of the Cepik service website. Defaults to "https://historiapojazdu.gov.pl/strona-glowna/".
        """
    driver: Chrome
    car_details: CarDetails
    vehicle_information = [VehicleHistoryInformation.MOT_STATUS, VehicleHistoryInformation.INSURANCE_STATUS]
    url: str = "https://historiapojazdu.gov.pl/strona-glowna/"

    def get_car_report(self):
        """
            Method: get_car_report

            This method retrieves a report for a car based on the car details and vehicle information provided.

            :return: A dictionary containing the car report information.
        """
        report = {}
        self.driver.get(self.url)
        registration = self.driver.find_element(by=By.ID,
                                                value="_historiapojazduportlet_WAR_historiapojazduportlet_:rej")
        registration.send_keys(self.car_details.registration)

        vin = self.driver.find_element(by=By.ID, value="_historiapojazduportlet_WAR_historiapojazduportlet_:vin")
        vin.send_keys(self.car_details.vin)

        self.driver.execute_script(
            f'document.getElementById("_historiapojazduportlet_WAR_historiapojazduportlet_:data").value="{self.car_details.first_registration_date}"')

        check_btn = self.driver.find_element(by=By.ID,
                                             value="_historiapojazduportlet_WAR_historiapojazduportlet_:btnSprawdz")
        check_btn.click()

        for information in self.vehicle_information:
            report[information] = self.driver.find_element(by=By.CSS_SELECTOR, value=information.value).text

        return report
