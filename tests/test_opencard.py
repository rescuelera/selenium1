from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = "/index.php?route=common/home"
    SLIDER = (By.CSS_SELECTOR, ".slideshow.swiper-viewport")
    BRAND_SWIPER = (By.CSS_SELECTOR, ".carousel.swiper-viewport")
    SLIDER_PAGINATION = (
    By.CSS_SELECTOR, ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
    FEATURED = (By.XPATH, "*//h3[contains(text(), 'Featured')]")


class TabletsPage:
    URL = "/tablet"
    TABLETS = (By.XPATH, "*//h2[contains(text(), 'Tablets')]")
    LIST_ICON = (By.CSS_SELECTOR, "#list-view")
    GRID_ICON = (By.CSS_SELECTOR, "#grid-view")
    CATALOG_NAVIGATION = (By.CSS_SELECTOR, "#column-left > .list-group")
    ACTIVE_NAVIGTION_ITEM = (
    By.CSS_SELECTOR, "#column-left > .list-group > .list-group-item.active[contains(text(),'Tablets')]")


class ItemViewPage:
    URL = "/tablet/samsung-galaxy-tab-10-1"
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "#button-cart.btn.btn-primary.btn-lg.btn-block")
    DESCRIPTION_TAB = (By.XPATH, "//li/a[.='Description']")
    IMAGE_ADDITIONAL = (By.CSS_SELECTOR, "li.image-additional")
    PRICE = (By.CSS_SELECTOR, "ul.list-unstyled > li >h2")
    ADD_WISH_LIST_BUTTON = (By.CSS_SELECTOR, "div.btn-group>button>i.fa.fa-heart")
    EXCHANGE_BUTTON = (By.CSS_SELECTOR, "div.btn-group>button>i.fa.fa-exchange")


class RegisterUserPage:
    URL = "/index.php?route=account/register"
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")


class AdminLoginPage:
    URL = "/admin/"
    INPUT_USER_NAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    HELP_BLOCK = (By.CSS_SELECTOR, "span.help-block")
    PANEL_TITLE = (By.CSS_SELECTOR, "h1.panel-title")


def wait_until_element_visible(driver, locator, sec: int = 4):
    WebDriverWait(driver, sec).until(EC.visibility_of_element_located(locator))


def wait_until_elements_visible(driver, locator, sec: int = 4):
    WebDriverWait(driver, sec).until(EC.visibility_of_all_elements_located(locator))


def test_main_page(driver, base_url):
    driver.get(base_url + MainPage.URL)
    wait_until_element_visible(driver, MainPage.SLIDER)
    wait_until_element_visible(driver, MainPage.FEATURED)
    wait_until_element_visible(driver, MainPage.BRAND_SWIPER)
    wait_until_element_visible(driver, MainPage.SLIDER_PAGINATION)
    assert "Your Store" == driver.title


def test_catalog_page(driver, base_url):
    driver.get(base_url + TabletsPage.URL)
    wait_until_element_visible(driver, TabletsPage.TABLETS)
    wait_until_element_visible(driver, TabletsPage.LIST_ICON)
    wait_until_element_visible(driver, TabletsPage.GRID_ICON)
    wait_until_element_visible(driver, TabletsPage.CATALOG_NAVIGATION)
    assert "Tablets" == driver.title


def test_item_view(driver, base_url):
    driver.get(base_url + ItemViewPage.URL)
    wait_until_element_visible(driver, ItemViewPage.ADD_TO_CARD_BUTTON)
    wait_until_element_visible(driver, ItemViewPage.DESCRIPTION_TAB)
    wait_until_elements_visible(driver, ItemViewPage.IMAGE_ADDITIONAL)
    wait_until_element_visible(driver, ItemViewPage.ADD_WISH_LIST_BUTTON)
    wait_until_element_visible(driver, ItemViewPage.EXCHANGE_BUTTON)


def test_register_user(driver, base_url):
    driver.get(base_url + RegisterUserPage.URL)
    wait_until_element_visible(driver, RegisterUserPage.INPUT_FIRST_NAME)
    wait_until_element_visible(driver, RegisterUserPage.INPUT_LAST_NAME)
    wait_until_element_visible(driver, RegisterUserPage.INPUT_EMAIL)
    wait_until_element_visible(driver, RegisterUserPage.INPUT_TELEPHONE)
    wait_until_element_visible(driver, RegisterUserPage.INPUT_PASSWORD)


def test_login_administration(driver, base_url):
    driver.get(base_url + AdminLoginPage.URL)
    wait_until_element_visible(driver, AdminLoginPage.INPUT_USER_NAME)
    wait_until_element_visible(driver, AdminLoginPage.INPUT_PASSWORD)
    wait_until_element_visible(driver, AdminLoginPage.LOGIN_BUTTON)
    wait_until_element_visible(driver, AdminLoginPage.HELP_BLOCK)
    wait_until_element_visible(driver, AdminLoginPage.PANEL_TITLE)
