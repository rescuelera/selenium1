import logging

import selenium
from selenium.common.exceptions import StaleElementReferenceException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
import allure


def visibility_of_element(locator):
    def _predicate(driver):
        try:
            element = driver.find_element(*locator)
            return element if element.is_displayed() else False
        except InvalidSelectorException as e:
            raise e
        except StaleElementReferenceException:
            return False

    return _predicate


class BasePage:
    @allure.step
    def goto_this_page(self):
        logging.info(f"Opening page {self.page_url}")
        self.driver.get(self.page_url)

    @allure.step
    def get_element(self, locator, timeout=4):
        logging.info(f"Try to find element {locator}")
        try:
            return WebDriverWait(self.driver, timeout).until(visibility_of_element(locator))
        except selenium.common.exceptions.TimeoutException:
            allure.attach(
                name=f"{locator}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element {locator} is not found")

    @allure.step
    def click_on_element(self, locator):
        element = self.get_element(locator)
        logging.info(f"Click on {locator}")
        element.click()

    @allure.step
    def clear_element(self, locator):
        element = self.get_element(locator)
        logging.info(f"Clear element {locator}")
        element.clear()

    @allure.step
    def send_keys_to_element(self, locator, input):
        element = self.get_element(locator)
        logging.info(f"Send keys {input} to {locator}")
        element.send_keys(input)

    @allure.step
    def get_title(self):
        logging.info(f"Get title {self.driver.title}")
        return self.driver.title
