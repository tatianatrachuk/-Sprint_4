from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import test_config as tc

class TestLogo:

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

    # @staticmethod
    @allure.step('Закрываем браузер')
    def quit_driver(self):
        self.driver.quit()

    @allure.title('Нажимаем на логотип "Самоката"')
    @allure.description(
        'На странице ищем и нажимаем на логотип "Самоката" и проверяет переход на главную страницу "Самоката"')
    def check_scooter_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoScooter__3lsAR').click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/', self.driver.quit()

    @allure.title('Нажимаем на логотип "Яндекса"')
    @allure.description(
        'На странице ищем и нажимаем на логотип "Яндекса" и проверяет, что в новом окне откроется главная страница Яндекса')
    def check_yandex_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoYandex__3TSOI').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', self.driver.quit()