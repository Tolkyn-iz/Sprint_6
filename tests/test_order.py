import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_success_page import OrderSuccessPage

@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("button_location, name, surname, address, metro_station, phone, "
                             "delivery_date, rental_period, color, comment", [
        ("top", "Анна", "Петрова", "ул. Ленина 10", "Кропоткинская", 
         "+79161234567", "25.10.2024", "сутки", "black", "Позвоните за час"),
        
        ("bottom", "Сергей", "Иванов", "пр. Мира 25", "Комсомольская", 
         "+79998887766", "26.10.2024", "трое суток", "grey", "Домофон 123")
    ])
    def test_create_order(self, driver, button_location, name, surname, address, 
                          metro_station, phone, delivery_date, rental_period, 
                          color, comment):
        
        home_page = HomePage(driver)
        
        # Выбор кнопки заказа в зависимости от параметра
        if button_location == "top":
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        order_page.create_order(name, surname, address, metro_station, phone,
                               delivery_date, rental_period, color, comment)
        
        success_page = OrderSuccessPage(driver)
        assert success_page.is_order_success_displayed(), "Заказ не был оформлен успешно"