import allure
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

    @allure.step
    def slider_is_visible(self) -> bool:
        return self.get_element(self.SLIDER).is_displayed()

    @allure.step
    def features_is_visible(self) -> bool:
        return self.get_element(self.FEATURED).is_displayed()

    @allure.step
    def brand_swiper_is_visible(self) -> bool:
        return self.get_element(self.BRAND_SWIPER).is_displayed()

    @allure.step
    def slider_pagination_is_visible(self) -> bool:
        return self.get_element(self.SLIDER_PAGINATION).is_displayed()

    @allure.step
    def click_switcher_currency(self):
        self.click_on_element(self.SWITCHER_CURRENCY)

    @allure.step
    def select_sterling_currency(self):
        self.click_on_element(self.STERLING_CURRENCY)

    @allure.step
    def sterling_currency_is_visible(self) -> bool:
        return self.get_element(self.STERLING_CURRENCY_SELECTED).is_displayed()
