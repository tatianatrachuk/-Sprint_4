from tests import urls as tc

class TestLogo:

    def test_scooter_logo(self, main_page, driver):
        driver = driver
        main_page.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_yandex_logo(self, main_page, base_page, driver):
        driver = driver
        main_page.click_yandex_logo()
        base_page.switch_window()
        base_page.wait_load_page(tc.yandex_dzen_url)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'