import allure
from pages.home_page import HomePage
from urls import Urls


@allure.feature("Логотипы")
class TestLogoRedirect:
    
    @allure.title("Клик на логотип Самоката - переход на главную страницу")
    def test_samokat_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_button_top()
        home_page.click_samokat_logo()
        
        with allure.step("Проверить, что вернулись на главную страницу"):
            assert home_page.get_current_url() == Urls.BASE_URL
    
    @allure.title("Клик на логотип Яндекса - открытие Дзена в новом окне")
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_yandex_logo_and_switch_to_new_window()
        
        with allure.step("Проверить, что открылся Дзен"):
            assert "dzen.ru" in home_page.get_current_url() or "yandex" in home_page.get_current_url()