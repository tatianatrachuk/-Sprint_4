import pytest
from selenium import webdriver
from base_page import BasePage
from question_page import QuestionsPage
from order_form_page import OrderPage
from main_page import MainPage
import test_config as tc

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(tc.base_url)

    yield driver
    driver.quit()

def test_question(driver):
    arrows = QuestionsPage(driver)
    base = BasePage(driver)
    base.accept_cookie()
    arrows.test_questions_main_page()

def test_one_positive_flow(driver):
    order = OrderPage(driver)
    base = BasePage(driver)
    base.accept_cookie()
    base.order_button()
    order.login(tc.name, tc.surname, tc.address, tc.subway, tc.phone, tc.scooter_color, tc.comment_for_the_courier)
    base.load_order_form()
    order.check_order()

def test_two_positive_flow(driver):
    order = OrderPage(driver)
    base = BasePage(driver)
    base.accept_cookie()
    order.order_button_two()
    order.login(tc.name_test2, tc.surname_test2, tc.address_test2, tc.subway_test2, tc.phone_test2, tc.scooter_color_test2, tc.comment_for_the_courier_test2)
    base.load_order_form()
    order.check_order()

def test_logo(driver):
    logo = MainPage(driver)
    base = BasePage(driver)
    base.accept_cookie()
    logo.click_scooter_logo()
    logo.check_scooter_logo()
    logo.click_yandex_logo()
    base.switch_window()
    base.wait_load_page()
    logo.check_yandex_logo()

