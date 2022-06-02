import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


DRIVERS = "E:\\AUTOMATION\\webdriver\\"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base-url", default="http://192.168.88.251:8081/")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "firefox":
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser_name == "chrome":
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "opera":
        options = Options()
        options.binary_location = r'C:\Users\booka-msi\AppData\Local\Programs\Opera\87.0.4390.25_0\opera.exe'
        browser = webdriver.Opera(options=options, executable_path=OperaDriverManager().install())
    else:
        raise ValueError("Wrong browser")

    browser.maximize_window()
    yield browser
    browser.close()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")
