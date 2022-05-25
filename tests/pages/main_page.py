from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.base_page import BasePage


class MainPage(BasePage):
    URL = "/index.php?route=common/home"
    SLIDER = (By.CSS_SELECTOR, ".slideshow.swiper-viewport")
    BRAND_SWIPER = (By.CSS_SELECTOR, ".carousel.swiper-viewport")
    SLIDER_PAGINATION = (
        By.CSS_SELECTOR, ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
    FEATURED = (By.XPATH, "*//h3[contains(text(), 'Featured')]")
    SWITCHER_CURRENCY = (By.XPATH, "*//button[@data-toggle='dropdown']/span[contains(text(), 'Currency')]")
    STERLING_CURRENCY = (By.XPATH, "*//button[@name='GBP']")
    STERLING_CURRENCY_SELECTED = (By.XPATH, "*//strong[contains(text(), '£')]")

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.page_url = base_url + self.URL

    def slider_is_visible(self) -> bool:
        element = self.driver.find_element(*self.SLIDER)
        return element.is_displayed()

    def features_is_visible(self) -> bool:
        element = self.driver.find_element(*self.FEATURED)
        return element.is_displayed()

    def brand_swiper_is_visible(self) -> bool:
        element = self.driver.find_element(*self.BRAND_SWIPER)
        return element.is_displayed()

    def slider_pagination_is_visible(self) -> bool:
        element = self.driver.find_element(*self.SLIDER_PAGINATION)
        return element.is_displayed()

    def get_title(self):
        return self.driver.title

    def click_switcher_currency(self):
        self.get_element(self.SWITCHER_CURRENCY).click()

    def select_sterling_currency(self):
        self.get_element(self.STERLING_CURRENCY).click()

    def sterling_currency_is_visible(self) -> bool:
        element = self.driver.find_element(*self.STERLING_CURRENCY_SELECTED)
        return element.is_displayed()
