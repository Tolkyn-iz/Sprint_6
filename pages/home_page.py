from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    # Локаторы кнопок заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')]")
    
    # Локаторы вопросов и ответов
    QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }
    
    ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }
    
    # Логотипы
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@href, '/')]//img[contains(@alt, 'Scooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_button_top(self):
        self.click_with_scroll(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        button = self.wait_for_clickable(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        self.click_by_js(button)

    @allure.step("Нажать на вопрос")
    def click_question(self, index):
        locator = self.QUESTIONS.get(index)
        if locator:
            element = self.find_element(locator)
            self.scroll_to_element(element)
            self.click_by_js(element)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        locator = self.ANSWERS.get(index)
        if locator:
            element = self.wait_for_visibility(locator)
            return element.text
        return ""

    @allure.step("Нажать на логотип Самоката")
    def click_samokat_logo(self):
        element = self.wait_for_clickable(self.SAMOKAT_LOGO)
        self.click_by_js(element)

    @allure.step("Нажать на логотип Яндекса и переключиться на новое окно")
    def click_yandex_logo_and_switch_to_new_window(self):
        element = self.wait_for_clickable(self.YANDEX_LOGO)
        element.click()
        self.switch_to_new_window()