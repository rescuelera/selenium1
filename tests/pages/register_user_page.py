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

    def input_first_name_is_visible(self) -> bool:
        element = self.driver.find_element(*self.INPUT_FIRST_NAME)
        return element.is_displayed()

    def input_last_name_is_visible(self) -> bool:
        element = self.driver.find_element(*self.INPUT_LAST_NAME)
        return element.is_displayed()

    def input_email_is_visible(self) -> bool:
        element = self.driver.find_element(*self.INPUT_EMAIL)
        return element.is_displayed()

    def input_telephone_is_visible(self) -> bool:
        element = self.driver.find_element(*self.INPUT_TELEPHONE)
        return element.is_displayed()

    def input_password_is_visible(self) -> bool:
        element = self.driver.find_element(*self.INPUT_PASSWORD)
        return element.is_displayed()

    def enter_first_name(self, name: str):
        self.get_element(self.INPUT_FIRST_NAME).click()
        self.get_element(self.INPUT_FIRST_NAME).clear()
        self.get_element(self.INPUT_FIRST_NAME).send_keys(name)

    def enter_last_name(self, last_name: str):
        self.get_element(self.INPUT_LAST_NAME).click()
        self.get_element(self.INPUT_LAST_NAME).clear()
        self.get_element(self.INPUT_LAST_NAME).send_keys(last_name)

    def enter_email(self, email: str):
        self.get_element(self.INPUT_EMAIL).click()
        self.get_element(self.INPUT_EMAIL).clear()
        self.get_element(self.INPUT_EMAIL).send_keys(email)

    def enter_telephone(self, telephone: str):
        self.get_element(self.INPUT_TELEPHONE).click()
        self.get_element(self.INPUT_TELEPHONE).clear()
        self.get_element(self.INPUT_TELEPHONE).send_keys(telephone)

    def enter_password(self, password: str):
        self.get_element(self.INPUT_PASSWORD).click()
        self.get_element(self.INPUT_PASSWORD).clear()
        self.get_element(self.INPUT_PASSWORD).send_keys(password)

    def confirm_password(self, password: str):
        self.get_element(self.INPUT_PASSWORD_CONFIRM).click()
        self.get_element(self.INPUT_PASSWORD_CONFIRM).clear()
        self.get_element(self.INPUT_PASSWORD_CONFIRM).send_keys(password)

    def click_policy_checkbox(self):
        self.get_element(self.POLICY_CHECKBOX).click()

    def click_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def account_created_is_visible(self) -> bool:
        element = self.driver.find_element(*self.ACCOUNT_CREATED)
        return element.is_displayed()
