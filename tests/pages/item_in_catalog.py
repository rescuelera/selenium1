from selenium.common.exceptions import InvalidSelectorException, StaleElementReferenceException
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

    def click_add_product(self):
        self.get_element(self.ADD_PRODUCT_BUTTON).click()

    def add_product_name(self, name: str):
        self.get_element(self.INPUT_PRODUCT_NAME).click()
        self.get_element(self.INPUT_PRODUCT_NAME).clear()
        self.get_element(self.INPUT_PRODUCT_NAME).send_keys(name)

    def add_product_desription(self, desription: str):
        self.get_element(self.INPUT_DESRIPTION).click()
        self.get_element(self.INPUT_DESRIPTION).clear()
        self.get_element(self.INPUT_DESRIPTION).send_keys(desription)

    def add_product_model(self, model: str):
        self.get_element(self.INPUT_MODEL).click()
        self.get_element(self.INPUT_MODEL).clear()
        self.get_element(self.INPUT_MODEL).send_keys(model)

    def add_product_mega_tag_title(self, model: str):
        self.get_element(self.META_TAG_TITLE).click()
        self.get_element(self.META_TAG_TITLE).clear()
        self.get_element(self.META_TAG_TITLE).send_keys(model)

    def click_data_tab(self):
        self.get_element(self.DATA_TAB).click()

    def click_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def click_catalog_tab(self):
        self.get_element(self.CATALOG).click()

    def click_products_tab(self):
        self.get_element(self.PRODUCTS).click()

    def select_checkdox_1(self):
        self.get_element(self.SELECT_CHECKBOX_1).click()

    def click_delete_button(self):
        self.get_element(self.DELETE_BUTTON).click()

    def accept_delete_alert(self):
        alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert.accept()
