import pytest
from tests_question_page import QuestionsPage
from order_form_page import OrderPage
from logo_page import TestLogo
import test_config as tc

@pytest.fixture(scope="module")
def arrows_fixture():
    arrows = QuestionsPage()
    arrows.setup_class()
    arrows.open_page()
    arrows.accept_cookie()
    yield arrows
    arrows.quit_driver()

@pytest.fixture(scope="module")
def order_fixture():
    order = OrderPage()
    order.setup_class()
    order.open_page()
    order.accept_cookie()
    yield order
    order.quit_driver()

@pytest.fixture(scope="module")
def logo_fixture():
    logo = TestLogo()
    logo.setup_class()
    logo.open_page()
    yield logo
    logo.quit_driver()

def test_questions_main_page(arrows_fixture):
    arrows_fixture.check_zero_arrow()
    arrows_fixture.check_first_arrow()
    arrows_fixture.check_second_arrow()
    arrows_fixture.check_third_arrow()
    arrows_fixture.check_fourth_arrow()
    arrows_fixture.check_fifth_arrow()
    arrows_fixture.check_sixth_arrow()
    arrows_fixture.check_seventh_arrow()

def test_one_positive_flow(order_fixture):
    order_fixture.order_button()
    order_fixture.login(tc.name, tc.surname, tc.address, tc.subway, tc.phone, tc.scooter_color, tc.comment_for_the_courier)

def test_two_positive_flow(order_fixture):
    order_fixture.order_button_two()
    order_fixture.login(tc.name_test2, tc.surname_test2, tc.address_test2, tc.subway_test2, tc.phone_test2, tc.scooter_color_test2, tc.comment_for_the_courier_test2)

def test_logo(logo_fixture):
    logo_fixture.check_scooter_logo()
    logo_fixture.check_yandex_logo()
