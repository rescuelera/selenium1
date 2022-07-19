import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage


class ItemInCatalog(BasePage):
    ADD_PRODUCT_BUTTON = (By.XPATH, "*//div/a[@data-original-title='Add New']")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_DESRIPTION = (By.XPATH, "*//div[@role='textbox']")
    INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
    SUBMIT_BUTTON = (By.XPATH, "*//button[@type='submit']")
    DATA_TAB = (By.XPATH, "*//a[@data-toggle='tab'][contains(text(), 'Data')]")
    CATALOG = (By.XPATH, "*//li/a[@data-toggle='collapse'][@class='parent collapsed'][contains(text(), 'Catalog')]")
    PRODUCTS = (By.XPATH, "*//ul[@id='collapse1']/li/a[contains(text(), 'Products')]")
    META_TAG_TITLE = (By.XPATH, "*//input[@type='text'][@name='product_description[1][meta_title]']")
    SELECT_CHECKBOX_1 = (By.XPATH, "(*//input[@type='checkbox'][@name='selected[]'])[1]")

    DELETE_BUTTON = (By.XPATH, "(*//button[@type='button'][@data-original-title='Delete'])")

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver

    @allure.step
    def click_add_product(self):
        self.click_on_element(self.ADD_PRODUCT_BUTTON)

    @allure.step
    def add_product_name(self, name: str):
        self.click_on_element(self.INPUT_PRODUCT_NAME)
        self.clear_element(self.INPUT_PRODUCT_NAME)
        self.send_keys_to_element(self.INPUT_PRODUCT_NAME, name)

    @allure.step
    def add_product_desription(self, desription: str):
        self.click_on_element(self.INPUT_DESRIPTION)
        self.clear_element(self.INPUT_DESRIPTION)
        self.send_keys_to_element(self.INPUT_DESRIPTION, desription)

    @allure.step
    def add_product_model(self, model: str):
        self.click_on_element(self.INPUT_MODEL)
        self.clear_element(self.INPUT_MODEL)
        self.send_keys_to_element(self.INPUT_MODEL, model)

    @allure.step
    def add_product_mega_tag_title(self, model: str):
        self.click_on_element(self.META_TAG_TITLE)
        self.clear_element(self.META_TAG_TITLE)
        self.send_keys_to_element(self.META_TAG_TITLE, model)

    @allure.step
    def click_data_tab(self):
        self.click_on_element(self.DATA_TAB)

    @allure.step
    def click_submit_button(self):
        self.click_on_element(self.SUBMIT_BUTTON)

    @allure.step
    def click_catalog_tab(self):
        self.click_on_element(self.CATALOG)

    @allure.step
    def click_products_tab(self):
        self.click_on_element(self.PRODUCTS)

    @allure.step
    def select_checkdox_1(self):
        self.click_on_element(self.SELECT_CHECKBOX_1)

    @allure.step
    def click_delete_button(self):
        self.click_on_element(self.DELETE_BUTTON)

    @allure.step
    def accept_delete_alert(self):
        alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert.accept()
