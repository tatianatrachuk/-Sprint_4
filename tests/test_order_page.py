
class TestOrderForm:

    def test_one_positive_flow(self, order_form_page, base_page):
        order_form_page.order_button()
        order_form_page.login(name='Татьяна', surname="Трачук", address="Лермонтова, 89", subway="Бульвар Рокоссовского",
        phone="895687894567", scooter_color="чёрный жемчуг", comment_for_the_courier="оставить у двери")
        base_page.load_order_form()
        accept_message = order_form_page.check_order()
        assert 'Заказ оформлен' in accept_message

    def test_two_positive_flow(self, order_form_page, base_page):
        order_form_page.order_button_two()
        order_form_page.login(name='Иван', surname="Смирнов", address="Крылова, 145", subway="Бульвар Рокоссовского",
                              phone="89567845609", scooter_color="серая безысходность", comment_for_the_courier="не звонить в дверьи")
        base_page.load_order_form()
        panel = order_form_page.successful_order_check()
        assert 'Заказ оформлен' == panel
