from dataclasses import dataclass
from typing import Self
from selenium.webdriver.chrome.options import Options


class ChromeOptionsBuilder:
    """
    A builder class for configuring ChromeOptions.

    Args:
        options (Options, optional): The base options. Defaults to Options().

    Returns:
        ChromeOptionsBuilder: An instance of ChromeOptionsBuilder.

    Methods:
        no_sandbox: Adds the '--no-sandbox' argument to the options.
        no_screen: Adds the '--headless' argument to the options.
        no_dev_shared_memory: Adds the '--disable-dev-shm-usage' argument to the options.
        build: Returns the built ChromeOptions.

    Example:
        options = ChromeOptionsBuilder()
            .no_sandbox()
            .no_screen()
            .no_dev_shared_memory()
            .build()
    """

    def __init__(self, options=Options) -> None:
        self.options = options()

    def no_sandbox(self) -> Self:
        """
        Apply the '--no-sandbox' option to the current instance of the WebDriver.

        :return: The current instance of the WebDriver with the '--no-sandbox' option applied.
        """
        self.options.add_argument('--no-sandbox')
        return self

    def no_screen(self) -> Self:
        """
        Set the headless option to True, indicating that the browser should run without a visible screen.

        :return: self - The current object instance.
        """
        self.options.add_argument('--headless')
        return self

    def no_dev_shared_memory(self) -> Self:
        """
        Disable dev-shm-usage option.

        :return: Self instance.
        """
        self.options.add_argument('--disable-dev-shm-usage')
        return self

    def build(self) -> Options:
        """
        Build the options and return them.

        :return: The built options.
        """
        return self.options
