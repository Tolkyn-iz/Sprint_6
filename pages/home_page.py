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

    def click_order_button_top(self):
        with allure.step("Нажать кнопку 'Заказать' вверху страницы"):
            self.click_with_scroll(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        with allure.step("Нажать кнопку 'Заказать' внизу страницы"):
            # Прокручиваем к кнопке
            button = self.wait_for_clickable(self.ORDER_BUTTON_BOTTOM)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            import time
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", button)

    def click_question(self, index):
        with allure.step(f"Нажать на вопрос {index}"):
            locator = self.QUESTIONS.get(index)
            if locator:
                element = self.find_element(locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                import time
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, index):
        with allure.step(f"Получить текст ответа на вопрос {index}"):
            locator = self.ANSWERS.get(index)
            if locator:
                element = self.wait_for_visibility(locator)
                return element.text
            return ""

    def click_samokat_logo(self):
        with allure.step("Нажать на логотип Самоката"):
            import time
            time.sleep(2)
            self.click_with_scroll(self.SAMOKAT_LOGO)

    def click_yandex_logo(self):
        with allure.step("Нажать на логотип Яндекса"):
            element = self.wait_for_clickable(self.YANDEX_LOGO)
            element.click()

    def get_current_url(self):
        return self.driver.current_url