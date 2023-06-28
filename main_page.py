from selenium.webdriver.common.by import By
import test_config as tc

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    scooter_logo = [By.ID, 'accordion__heading-0']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    def check_scooter_logo(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def check_yandex_logo(self):
        assert self.driver.current_url == tc.excpected_url


