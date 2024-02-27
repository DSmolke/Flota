from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# noinspection PyUnresolvedReferences
from app.service.drivers import ChromeDriverLinux
# noinspection PyUnresolvedReferences
from app.service.options_builder import ChromeOptionsBuilder

options = ChromeOptionsBuilder().no_sandbox().no_screen().no_dev_shared_memory().build()
driver_linux = ChromeDriverLinux(options, Service(service=ChromeDriverManager().install())).create()
