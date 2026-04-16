from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class OrderSuccessPage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")

    def is_order_success_displayed(self):
        with allure.step("Проверить, что появилось сообщение об успешном заказе"):
            try:
                self.wait_for_visibility(self.SUCCESS_MESSAGE)
                return True
            except:
                return False

    def get_success_message_text(self):
        return self.find_element(self.SUCCESS_MESSAGE).text