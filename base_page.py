from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    accept_cookies = [By.ID, 'rcc-confirm-button']
    load_form = [By.CLASS_NAME, "Order_Modal__YZ-d3"]

    @allure.title('Принятие cookie')
    @allure.description(
        'На странице ищем текст "И здесь куки! В общем, мы их используем." и нажимаем на кнопку "да все привыкли"')
    def accept_cookie(self):
        self.driver.find_element(*self.accept_cookies).click()

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидаем открытие нужной страницы и переход на нее')
    def wait_load_page(self, yandex_dzen_url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(yandex_dzen_url))

    def load_order_form(self, load_form):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(*self.load_form))
