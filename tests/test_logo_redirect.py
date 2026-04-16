import allure
import time
from pages.home_page import HomePage

@allure.feature("Логотипы")
class TestLogoRedirect:
    
    @allure.title("Клик на логотип Самоката - переход на главную страницу")
    def test_samokat_logo_redirect(self, driver, base_url):
        home_page = HomePage(driver)
        home_page.click_order_button_top()
        home_page.click_samokat_logo()
        
        with allure.step("Проверить, что вернулись на главную страницу"):
            assert home_page.get_current_url() == base_url, \
                f"Ожидался URL: {base_url}, получен: {home_page.get_current_url()}"
    
    @allure.title("Клик на логотип Яндекса - открытие Дзена в новом окне")
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.click_yandex_logo()
        
        time.sleep(2)
        
        original_window = driver.current_window_handle
        all_windows = driver.window_handles
        
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                break
        
        with allure.step("Проверить, что открылся Дзен"):
            current_url = driver.current_url
            assert "dzen.ru" in current_url or "yandex" in current_url, \
                f"Открылся не Дзен. Текущий URL: {current_url}"