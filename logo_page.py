from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import test_config as tc

class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.driver = cls.init_driver()

    @staticmethod
    @allure.step('Открываем браузер Firefox')
    def init_driver():
        return webdriver.Firefox()

    @allure.step(f'Открываем страницу {tc.base_url}')
    def open_page(self):
        self.driver.get(tc.base_url)

    @allure.step('Закрываем браузер')
    def quit_driver(self):
        self.driver.quit()


class TestLogo(BaseTest):
    def check_scooter_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoScooter__3lsAR').click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/', self.driver.quit()

    def check_yandex_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoYandex__3TSOI').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', self.driver.quit()