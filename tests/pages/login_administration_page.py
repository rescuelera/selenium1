from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.base_page import BasePage


class LoginAdministrationPage(BasePage):
    URL = "/admin/"
    INPUT_USER_NAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    HELP_BLOCK = (By.CSS_SELECTOR, "span.help-block")
    PANEL_TITLE = (By.CSS_SELECTOR, "h1.panel-title")

    ADMIN_LOGIN = "user"
    ADMIN_PASSWORD = "bitnami"

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.page_url = base_url + self.URL

    def input_username_is_visible(self) -> bool:
        return self.driver.find_element(*self.INPUT_USER_NAME).is_displayed()

    def input_password_is_visible(self) -> bool:
        return self.driver.find_element(*self.INPUT_PASSWORD).is_displayed()

    def login_button_is_visible(self) -> bool:
        return self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()

    def help_block_is_visible(self) -> bool:
        return self.driver.find_element(*self.HELP_BLOCK).is_displayed()

    def panel_title_is_visible(self) -> bool:
        return self.driver.find_element(*self.PANEL_TITLE).is_displayed()

    def enter_login(self):
        self.get_element(self.INPUT_USER_NAME).click()
        self.get_element(self.INPUT_USER_NAME).clear()
        self.get_element(self.INPUT_USER_NAME).send_keys(self.ADMIN_LOGIN)

    def enter_password(self):
        self.get_element(self.INPUT_PASSWORD).click()
        self.get_element(self.INPUT_PASSWORD).clear()
        self.get_element(self.INPUT_PASSWORD).send_keys(self.ADMIN_PASSWORD)

    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()
