from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_config as tc
import allure

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

class OrderPage(BaseTest):

    name_field = [By.XPATH, '//*[@placeholder="* Имя"]']
    surname_field = [By.XPATH, '//*[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
    subway_field = [By.XPATH, '//*[@placeholder="* Станция метро"]']
    choose_subway_field = [By.CLASS_NAME, 'select-search__select']
    phone_field = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
    button = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    comment_for_the_courier = [By.XPATH, '//*[@placeholder="Комментарий для курьера"]']
    rental_date = [By.CLASS_NAME, 'react-datepicker-wrapper']
    choose_rental_date = [By.CLASS_NAME, 'react-datepicker__day react-datepicker__day--015']
    rental_period = [By.CLASS_NAME, 'Dropdown-control']
    choose_rental_period = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]']
    button_order = [By.XPATH, 'Button_Button__ra12g Button_Middle__1CSJM']
    button_confirm = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]']
    order_form = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']


    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def set_subway(self, subway):
        self.driver.find_element(*self.subway_field).send_keys(subway)
        self.driver.find_element(*self.choose_subway_field).click()


    def set_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)


    def button_further(self):
        self.driver.find_element(*self.button).click()

    def rental_date(self):
        self.driver.find_element(*self.rental_date).click()
        self.driver.find_element(*self.choose_rental_date).click()

    def rental_period(self):
        self.driver.find_element(*self.choose_rental).click()
        self.driver.find_element(*self.choose_rental_period).click()

    def scooter_color(self, scooter_color):
        if scooter_color == 'чёрный жемчуг':
            self.driver.find_element(By.ID, 'black').click()
        if scooter_color == 'серая безысходность':
            self.driver.find_element(By.ID, 'grey').click()

    def comment_field(self, comment_for_the_courier):
        if len(comment_for_the_courier) != 0:
            self.driver.find_element(*self.comment_for_the_courier).send_keys(tc.comment_for_the_courier)

    def button_in_order(self):
        self.driver.find_element(*self.button_order).click()


    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "Order_ModalHeader__3FDaJ")))
        self.driver.find_element(*self.button_confirm).click()

    def load_order_form(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "Order_Modal__YZ-d3")))

    def check_order(self):
        assert 'Заказ оформлен' in self.driver.find_element(*self.order_form).text


    @allure.title('Заполняем форму заказа')
    @allure.description('На странице ищем элементы и заполняем поле соответсвуйющей информацией из файла test_config.py')
    def login(self, name, surname, address, subway, phone, scooter_color, comment_for_the_courier):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone(phone)
        self.button_further()
        self.rental_date()
        self.rental_period()
        self.scooter_color(scooter_color)
        self.comment_field(comment_for_the_courier)
        self.button_in_order()
        self.confirm_order()
        self.load_order_form
        self.check_order()

    @allure.title('Принятие cookie')
    @allure.description(
        'На странице ищем текст "И здесь куки! В общем, мы их используем." и нажимаем на кнопку "да все привыкли"')
    def accept_cookie(self):
        self.driver.find_element(By.ID, 'rcc-confirm-button').click()

    @allure.step('Нажимаем кнопку "Заказать" в хэдере')
    def order_button(self):
        self.driver.find_element(By.CLASS_NAME, 'Button_Button__ra12g').click()

    def successful_order_check(self):
        panel = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')))
        expected_text = 'Заказ оформлен'
        assert expected_text == panel.text, self.driver.quit()

    @allure.step('Нажимаем кнопку "Заказать" внизу страницы')
    def order_button_two(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button")))
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[4]/div[2]/div[5]/button').click()