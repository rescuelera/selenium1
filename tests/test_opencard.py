import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.catalog_page import CatalogPage
from tests.pages.item_view_page import ItemViewPage
from tests.pages.login_administration_page import LoginAdministrationPage
from tests.pages.main_page import MainPage
from tests.pages.item_in_catalog import ItemInCatalog
from tests.pages.register_user_page import RegisterUserPage

# def wait_until_element_visible(driver, locator, sec: int = 4):
#     element = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(locator))
#
#
# def wait_until_elements_visible(driver, locator, sec: int = 4):
#     WebDriverWait(driver, sec).until(EC.visibility_of_all_elements_located(locator))
from utils.utils import random_email


def test_main_page(driver, base_url):
    main_page = MainPage(driver, base_url)
    main_page.goto_this_page()
    assert main_page.slider_is_visible()
    assert main_page.features_is_visible()
    assert main_page.brand_swiper_is_visible()
    assert main_page.slider_pagination_is_visible()
    assert "Your Store" == main_page.get_title()


def test_catalog_page(driver, base_url):
    catalog_page = CatalogPage(driver, base_url)
    catalog_page.goto_this_page()
    assert catalog_page.tablets_is_visible()
    assert catalog_page.list_icon_is_visible()
    assert catalog_page.grid_icon_is_visible()
    assert catalog_page.catalog_navigation_is_visible()
    assert "Tablets" == catalog_page.get_title()


def test_item_view(driver, base_url):
    item_view_page = ItemViewPage(driver, base_url)
    item_view_page.goto_this_page()
    assert item_view_page.add_to_card_button_is_visible()
    assert item_view_page.description_tab_is_visible()
    assert item_view_page.image_additional_is_visible()
    assert item_view_page.add_wish_list_button_is_visible()
    assert item_view_page.exchange_button_is_visible()


def test_register_user(driver, base_url):
    register_user_page = RegisterUserPage(driver, base_url)
    register_user_page.goto_this_page()
    assert register_user_page.input_first_name_is_visible()
    assert register_user_page.input_first_name_is_visible()
    assert register_user_page.input_email_is_visible()
    assert register_user_page.input_telephone_is_visible()
    assert register_user_page.input_password_is_visible()
    register_user_page.enter_first_name("Name")
    register_user_page.enter_last_name("Familia")
    register_user_page.enter_email(random_email())
    register_user_page.enter_telephone("0000000000")
    register_user_page.enter_password("password")
    register_user_page.confirm_password("password")
    register_user_page.click_policy_checkbox()
    register_user_page.click_submit_button()
    assert register_user_page.account_created_is_visible()


def test_login_administration(driver, base_url):

    login_administration_page = LoginAdministrationPage(driver, base_url)
    login_administration_page.goto_this_page()
    assert login_administration_page.input_username_is_visible()
    assert login_administration_page.input_password_is_visible()
    assert login_administration_page.login_button_is_visible()
    assert login_administration_page.help_block_is_visible()
    assert login_administration_page.panel_title_is_visible()

def test_change_currency(driver, base_url):
    main_page = MainPage(driver, base_url)
    main_page.goto_this_page()
    main_page.click_switcher_currency()
    main_page.select_sterling_currency()
    assert main_page.sterling_currency_is_visible()

def test_add_new_item_for_administration(driver, base_url):
    login_administration_page = LoginAdministrationPage(driver, base_url)
    login_administration_page.goto_this_page()
    login_administration_page.enter_login()
    login_administration_page.enter_password()
    login_administration_page.click_login_button()
    item_in_catalog_page = ItemInCatalog(driver, base_url)
    item_in_catalog_page.click_catalog_tab()
    item_in_catalog_page.click_products_tab()
    item_in_catalog_page.click_add_product()
    item_in_catalog_page.add_product_name("Name")
    item_in_catalog_page.add_product_desription("Desription")
    item_in_catalog_page.add_product_mega_tag_title("Mega Tag Title")
    item_in_catalog_page.click_data_tab()
    item_in_catalog_page.add_product_model("Model")
    item_in_catalog_page.click_submit_button()


def test_delete_item_for_administration(driver, base_url):
    login_administration_page = LoginAdministrationPage(driver, base_url)
    login_administration_page.goto_this_page()
    login_administration_page.enter_login()
    login_administration_page.enter_password()
    login_administration_page.click_login_button()
    item_in_catalog_page = ItemInCatalog(driver, base_url)
    item_in_catalog_page.click_catalog_tab()
    item_in_catalog_page.click_products_tab()
    item_in_catalog_page.select_checkdox_1()
    item_in_catalog_page.click_delete_button()
    item_in_catalog_page.accept_delete_alert()
