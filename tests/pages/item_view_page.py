import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.base_page import BasePage


class ItemViewPage(BasePage):
    URL = "/tablet/samsung-galaxy-tab-10-1"
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "#button-cart.btn.btn-primary.btn-lg.btn-block")
    DESCRIPTION_TAB = (By.XPATH, "//li/a[.='Description']")
    IMAGE_ADDITIONAL = (By.CSS_SELECTOR, "li.image-additional")
    PRICE = (By.CSS_SELECTOR, "ul.list-unstyled > li >h2")
    ADD_WISH_LIST_BUTTON = (By.CSS_SELECTOR, "div.btn-group>button>i.fa.fa-heart")
    EXCHANGE_BUTTON = (By.CSS_SELECTOR, "div.btn-group>button>i.fa.fa-exchange")

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.page_url = base_url + self.URL

    @allure.step
    def add_to_card_button_is_visible(self) -> bool:
        return self.get_element(self.ADD_TO_CARD_BUTTON).is_displayed()

    @allure.step
    def description_tab_is_visible(self) -> bool:
        return self.get_element(self.DESCRIPTION_TAB).is_displayed()

    @allure.step
    def image_additional_is_visible(self) -> bool:
        return self.get_element(self.IMAGE_ADDITIONAL).is_displayed()

    @allure.step
    def price_is_visible(self) -> bool:
        return self.get_element(self.PRICE).is_displayed()

    @allure.step
    def add_wish_list_button_is_visible(self) -> bool:
        return self.get_element(self.ADD_WISH_LIST_BUTTON).is_displayed()

    @allure.step
    def exchange_button_is_visible(self) -> bool:
        return self.get_element(self.EXCHANGE_BUTTON).is_displayed()
