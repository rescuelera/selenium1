from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.base_page import BasePage


class CatalogPage(BasePage):
    URL = "/tablet"
    TABLETS = (By.XPATH, "*//h2[contains(text(), 'Tablets')]")
    LIST_ICON = (By.CSS_SELECTOR, "#list-view")
    GRID_ICON = (By.CSS_SELECTOR, "#grid-view")
    CATALOG_NAVIGATION = (By.CSS_SELECTOR, "#column-left > .list-group")
    ACTIVE_NAVIGATION_ITEM = (
        By.CSS_SELECTOR, "#column-left > .list-group > .list-group-item.active[contains(text(),'Tablets')]")

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.page_url = base_url + self.URL

    def tablets_is_visible(self) -> bool:
        return self.driver.find_element(*self.TABLETS).is_displayed()

    def list_icon_is_visible(self) -> bool:
        return self.driver.find_element(*self.LIST_ICON).is_displayed()

    def grid_icon_is_visible(self) -> bool:
        return self.driver.find_element(*self.GRID_ICON).is_displayed()

    def catalog_navigation_is_visible(self) -> bool:
        return self.driver.find_element(*self.CATALOG_NAVIGATION).is_displayed()

    def get_title(self):
        return self.driver.title
