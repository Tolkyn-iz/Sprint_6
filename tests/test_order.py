import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_success_page import OrderSuccessPage
from data import ORDER_DATA_TOP_BUTTON, ORDER_DATA_BOTTOM_BUTTON


@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката через верхнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, metro_station, phone, "
                             "delivery_date, rental_period, color, comment", 
                             ORDER_DATA_TOP_BUTTON)
    def test_create_order_top_button(self, driver, name, surname, address,
                                      metro_station, phone, delivery_date, 
                                      rental_period, color, comment):
        home_page = HomePage(driver)
        home_page.click_order_button_top()
        
        order_page = OrderPage(driver)
        order_page.create_order(name, surname, address, metro_station, phone,
                               delivery_date, rental_period, color, comment)
        
        success_page = OrderSuccessPage(driver)
        assert success_page.is_order_success_displayed(), "Заказ не был оформлен успешно"
    
    @allure.title("Позитивный сценарий заказа самоката через нижнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, metro_station, phone, "
                             "delivery_date, rental_period, color, comment", 
                             ORDER_DATA_BOTTOM_BUTTON)
    def test_create_order_bottom_button(self, driver, name, surname, address,
                                         metro_station, phone, delivery_date, 
                                         rental_period, color, comment):
        home_page = HomePage(driver)
        home_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        order_page.create_order(name, surname, address, metro_station, phone,
                               delivery_date, rental_period, color, comment)
        
        success_page = OrderSuccessPage(driver)
        assert success_page.is_order_success_displayed(), "Заказ не был оформлен успешно"