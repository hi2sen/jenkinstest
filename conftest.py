
import settings
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.pom.pages.country_page import CountryPage
from src.pom.pages.home_page import HomePage
from src.pom.pages.results_page import ResultsPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=settings.browser,
        choices=("chrome", "firefox", "headless"),
    )

@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture
def get_driver(request, get_browser):
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    request.cls.country_page = CountryPage(driver)
    request.cls.home_page = HomePage(driver)
    request.cls.results_page = ResultsPage(driver)
    driver.get(settings.url)
    try:
        yield driver
    finally:
        driver.quit()
