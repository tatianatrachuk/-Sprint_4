from tests_question_page import TestArrows
from order_form_page import OrderPage
from logo_page import TestLogo

def test_test_class():
    tests_question = TestArrows()
    tests_question.setup_class()
    tests_question.open_page()
    tests_question.accept_cookie()

    tests_question.check_zero_arrow()
    tests_question.check_first_arrow()
    tests_question.check_second_arrow()
    tests_question.check_third_arrow()
    tests_question.check_fourth_arrow()
    tests_question.check_fifth_arrow()
    tests_question.check_sixth_arrow()
    tests_question.check_seventh_arrow()
    tests_question.quit_driver()

def test_one_positive_flow():
    order = OrderPage()
    order.setup_class()
    order.open_page()
    order.accept_cookie()

    order.order_button()
    order.login()


    order.quit_driver()


def test_two_positive_flow():
    order = OrderPage()
    order.setup_class()
    order.open_page()
    order.accept_cookie()

    order.order_button_two()
    order.login_other_data()

    order.quit_driver()


def test_logo():
    logo = TestLogo()
    logo.setup_class()
    logo.open_page()

    logo.check_scooter_logo()
    logo.check_yandex_logo()
    logo.quit_driver()
