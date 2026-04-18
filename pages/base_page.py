from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидать видимость элемента")
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть с прокруткой")
    def click_with_scroll(self, locator):
        element = self.wait_for_clickable(locator)
        self.scroll_to_element(element)
        element.click()

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait_for_visibility(locator)

    @allure.step("Кликнуть через JavaScript")
    def click_by_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break