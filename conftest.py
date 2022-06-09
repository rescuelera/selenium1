import allure
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
    parser.addoption("--executor", default="local")
    parser.addoption("--base-url", default="http://192.168.88.231:8081/")
    parser.addoption("--browser_version", default=None)


@pytest.fixture
def driver(request):
    executor=request.config.getoption("--executor")
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    if executor=="local":
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
    else:
        executor_url=f"http://{executor}:4444/wd/hub"
        caps={
            "browserName": browser_name,
            "browserVersion": browser_version,
            "screenResolution": "1280x720"
        }
        browser=webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
        )
    browser.maximize_window()
    with allure.step(f"browser {browser_name} {browser_version}"):
        yield browser
    browser.close()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")
