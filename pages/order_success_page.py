from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderSuccessPage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_success_displayed(self):
        try:
            self.wait_for_visibility(self.SUCCESS_MESSAGE)
            return True
        except:
            return False