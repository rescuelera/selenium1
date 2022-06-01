from selenium.common.exceptions import StaleElementReferenceException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait


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
    def goto_this_page(self):
        self.driver.get(self.page_url)

    def get_element(self, locator, timeout=4):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element(locator))
