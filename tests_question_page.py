from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import test_config as tc

class TestArrows:

    @classmethod
    def setup_class(cls):
        cls.driver = cls.init_driver()

    zero_arrow = [By.ID, 'accordion__heading-0']
    first_arrow = [By.ID, 'accordion__heading-1']
    second_arrow = [By.ID, 'accordion__heading-2']
    third_arrow = [By.ID, 'accordion__heading-3']
    fourth_arrow = [By.ID, 'accordion__heading-4']
    fifth_arrow = [By.ID, 'accordion__heading-5']
    sixth_arrow = [By.ID, 'accordion__heading-6']
    seventh_arrow = [By.ID, 'accordion__heading-7']

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

    @allure.title('Проверка первого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-0"и проверяем, что открывается соответствующий текст')
    def check_zero_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2200)')
        WebDriverWait(self.driver, 20)
        self.driver.find_element(*self.zero_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-0')))
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert expected_text == panel_0.text, 'FAILED'

    @allure.title('Проверка второго вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-1"и проверяем, что открывается соответствующий текст')
    def check_first_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.first_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-1')))
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert expected_text == panel_0.text

    @allure.title('Проверка третьего вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-2"и проверяем, что открывается соответствующий текст')
    def check_second_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.second_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-2')))
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert expected_text == panel_0.text

    @allure.title('Проверка четвертого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-3"и проверяем, что открывается соответствующий текст')
    def check_third_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.third_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-3')))
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert expected_text == panel_0.text

    @allure.title('Проверка пятого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-4"и проверяем, что открывается соответствующий текст')
    def check_fourth_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.fourth_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-4')))
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert expected_text == panel_0.text

    @allure.title('Проверка шестого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-5"и проверяем, что открывается соответствующий текст')
    def check_fifth_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.fifth_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-5')))
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert expected_text == panel_0.text

    @allure.title('Проверка седьмого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-6"и проверяем, что открывается соответствующий текст')
    def check_sixth_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.sixth_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-6')))
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert expected_text == panel_0.text

    @allure.title('Проверка восьмого вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на элемент "accordion__heading-7"и проверяем, что открывается соответствующий текст')
    def check_seventh_arrow(self):

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*self.seventh_arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel_0 = wait.until(EC.presence_of_element_located((By.ID, 'accordion__panel-7')))
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert expected_text == panel_0.text

    @allure.title('Принятие cookie')
    @allure.description(
        'На странице ищем текст "И здесь куки! В общем, мы их используем." и нажимаем на кнопку "да все привыкли"')
    def accept_cookie(self):
        self.driver.find_element(By.ID, 'rcc-confirm-button').click()

