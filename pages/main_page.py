from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):

    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

