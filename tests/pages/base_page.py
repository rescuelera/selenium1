from selenium.common.exceptions import StaleElementReferenceException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
import random
import string


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


def random_string(string_len=7):
    sets = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choices(sets, k=string_len))


def random_email():
    return 'ex_test_' + random_string(string_len=12) + "@yopmail.com"


class BasePage:
    def goto_this_page(self):
        self.driver.get(self.page_url)

    def get_element(self, locator, timeout=4):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element(locator))
