import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_form_page import OrderPage
from pages.main_page import MainPage
from tests import urls as tc


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.get(tc.base_url)

    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def base_page(driver):
    base_page = BasePage(driver)
    base_page.accept_cookie()
    return base_page

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def order_form_page(driver):
    order_form_page = OrderPage(driver)
    return order_form_page