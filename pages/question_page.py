from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class QuestionsPage(BasePage):

    arrows = [
        [By.ID, 'accordion__heading-0'],
        [By.ID, 'accordion__heading-1'],
        [By.ID, 'accordion__heading-2'],
        [By.ID, 'accordion__heading-3'],
        [By.ID, 'accordion__heading-4'],
        [By.ID, 'accordion__heading-5'],
        [By.ID, 'accordion__heading-6'],
        [By.ID, 'accordion__heading-7']
    ]

    actual_questions = [
        [By.ID, 'accordion__panel-0'],
        [By.ID, 'accordion__panel-1'],
        [By.ID, 'accordion__panel-2'],
        [By.ID, 'accordion__panel-3'],
        [By.ID, 'accordion__panel-4'],
        [By.ID, 'accordion__panel-5'],
        [By.ID, 'accordion__panel-6'],
        [By.ID, 'accordion__panel-7']
    ]

    @allure.title('Проверка вопроса в разделе "Вопросы о важном"')
    @allure.description(
        'На странице ищем и нажимаем на соответствующий элемент и проверяем, что открывается соответствующий текст')
    def check_arrow(self, arrow_index, expected_texts):
        arrow = self.arrows[arrow_index]
        actual_question = self.actual_questions[arrow_index]
        expected_text = expected_texts[arrow_index]

        self.driver.execute_script('window.scrollBy(0, 2100)')
        self.driver.find_element(*arrow).click()
        wait = WebDriverWait(self.driver, 15)
        panel = wait.until(EC.presence_of_element_located((actual_question)))
        return expected_text, panel