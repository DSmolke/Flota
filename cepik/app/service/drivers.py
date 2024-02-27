from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

@dataclass
class ChromeDriver:
    """
    The ChromeDriver class is used to create a Chrome instance with specified Chrome options.

    :param chrome_options: The options to configure the Chrome instance.
    :type chrome_options: Options
    :param driver_base: The base WebDriver class to use. Default is Chrome.
    :type driver_base: WebDriver
    """
    chrome_options: Options
    driver_base = Chrome

    def create(self) -> Chrome:
        """
        Create a Chrome instance with the specified Chrome options.

        :return: A Chrome instance created with the specified Chrome options.
        """
        return self.driver_base(self.chrome_options)

@dataclass
class ChromeDriverLinux(ChromeDriver):
    """

    :class:`ChromeDriverLinux` class
    ==================================

    The :class:`ChromeDriverLinux` class is a subclass of :class:`ChromeDriver` that is specialized for Linux operating systems. It takes an instance of the :class:`Service` class as a parameter
    * in its constructor.


       Make sure you have the necessary dependencies and setup to use the ChromeDriver on Linux before using this class.

    Methods
    -------
    """
    service: Service

    def create(self) -> Chrome:
        """
        Creates a Chrome driver with the specified options and service.

        :return: The created Chrome driver.
        """
        return self.driver_base(options=self.chrome_options, service=self.service)