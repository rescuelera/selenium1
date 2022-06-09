import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.base_page import BasePage


class RegisterUserPage(BasePage):
    URL = "/index.php?route=account/register"
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    SUBMIT_BUTTON = (By.XPATH, "*//input[@type='submit'][@value='Continue']")
    POLICY_CHECKBOX = (By.XPATH, "*//input[@type='checkbox'][@name='agree'][@value=1]")
    ACCOUNT_CREATED = (By.XPATH, "*//div[@id='content']/h1[contains(text(),'Your Account Has Been Created!')]")

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.page_url = base_url + self.URL

    @allure.step
    def input_first_name_is_visible(self) -> bool:
        return self.get_element(self.INPUT_FIRST_NAME).is_displayed()

    @allure.step
    def input_last_name_is_visible(self) -> bool:
        return self.get_element(self.INPUT_LAST_NAME).is_displayed()

    @allure.step
    def input_email_is_visible(self) -> bool:
        return self.get_element(self.INPUT_EMAIL).is_displayed()

    @allure.step
    def input_telephone_is_visible(self) -> bool:
        return self.get_element(self.INPUT_TELEPHONE).is_displayed()

    @allure.step
    def input_password_is_visible(self) -> bool:
        return self.get_element(self.INPUT_PASSWORD).is_displayed()

    @allure.step
    def enter_first_name(self, name: str):
        self.click_on_element(self.INPUT_FIRST_NAME)
        self.clear_element(self.INPUT_FIRST_NAME)
        self.send_keys_to_element(self.INPUT_FIRST_NAME, name)

    @allure.step
    def enter_last_name(self, last_name: str):
        self.click_on_element(self.INPUT_LAST_NAME)
        self.clear_element(self.INPUT_LAST_NAME)
        self.send_keys_to_element(self.INPUT_LAST_NAME, last_name)

    @allure.step
    def enter_email(self, email: str):
        self.click_on_element(self.INPUT_EMAIL)
        self.clear_element(self.INPUT_EMAIL)
        self.send_keys_to_element(self.INPUT_EMAIL, email)

    @allure.step
    def enter_telephone(self, telephone: str):
        self.click_on_element(self.INPUT_TELEPHONE)
        self.clear_element(self.INPUT_TELEPHONE)
        self.send_keys_to_element(self.INPUT_TELEPHONE, telephone)

    @allure.step
    def enter_password(self, password: str):
        self.click_on_element(self.INPUT_PASSWORD)
        self.clear_element(self.INPUT_PASSWORD)
        self.send_keys_to_element(self.INPUT_PASSWORD, password)

    @allure.step
    def confirm_password(self, password: str):
        self.click_on_element(self.INPUT_PASSWORD_CONFIRM)
        self.clear_element(self.INPUT_PASSWORD_CONFIRM)
        self.send_keys_to_element(self.INPUT_PASSWORD_CONFIRM, password)

    @allure.step
    def click_policy_checkbox(self):
        self.click_on_element(self.POLICY_CHECKBOX)

    @allure.step
    def click_submit_button(self):
        self.click_on_element(self.SUBMIT_BUTTON)

    @allure.step
    def account_created_is_visible(self) -> bool:
        return self.get_element(self.ACCOUNT_CREATED).is_displayed()
