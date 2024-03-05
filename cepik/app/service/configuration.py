from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# noinspection PyUnresolvedReferences
from app.service.drivers import ChromeDriverLinux
# noinspection PyUnresolvedReferences
from app.service.options_builder import ChromeOptionsBuilder

options = ChromeOptionsBuilder().no_sandbox().no_screen().no_dev_shared_memory().download_pdf().build()
driver_linux = ChromeDriverLinux(options, Service(service=ChromeDriverManager().install())).create()
