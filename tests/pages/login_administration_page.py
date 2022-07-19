import allure
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

    @allure.step
    def input_username_is_visible(self) -> bool:
        return self.get_element(self.INPUT_USER_NAME).is_displayed()

    @allure.step
    def input_password_is_visible(self) -> bool:
        return self.get_element(self.INPUT_PASSWORD).is_displayed()

    @allure.step
    def login_button_is_visible(self) -> bool:
        return self.get_element(self.LOGIN_BUTTON).is_displayed()

    @allure.step
    def help_block_is_visible(self) -> bool:
        return self.get_element(self.HELP_BLOCK).is_displayed()

    @allure.step
    def panel_title_is_visible(self) -> bool:
        return self.get_element(self.PANEL_TITLE).is_displayed()

    @allure.step
    def enter_login(self):
        self.click_on_element(self.INPUT_USER_NAME)
        self.clear_element(self.INPUT_USER_NAME)
        self.send_keys_to_element(self.INPUT_USER_NAME, self.ADMIN_LOGIN)

    @allure.step
    def enter_password(self):
        self.click_on_element(self.INPUT_PASSWORD)
        self.clear_element(self.INPUT_PASSWORD)
        self.send_keys_to_element(self.INPUT_PASSWORD, self.ADMIN_PASSWORD)

    @allure.step
    def click_login_button(self):
        self.click_on_element(self.LOGIN_BUTTON)
