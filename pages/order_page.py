from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure
import time

class OrderPage(BasePage):
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Форма "Про аренду"
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    COLOR_GREY = (By.XPATH, "//label[@for='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Куки-баннер
    COOKIE_CLOSE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")

    def close_cookie_banner(self):
        with allure.step("Закрыть куки-баннер"):
            try:
                time.sleep(1)
                close_button = self.driver.find_element(*self.COOKIE_CLOSE_BUTTON)
                if close_button.is_displayed():
                    close_button.click()
                    time.sleep(0.5)
            except:
                pass

    def fill_first_form(self, name, surname, address, metro_station, phone):
        with allure.step(f"Заполнить первую форму"):
            self.close_cookie_banner()
            
            self.wait_for_visibility(self.NAME_INPUT).send_keys(name)
            self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
            self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
            
            metro_input = self.driver.find_element(*self.METRO_STATION_INPUT)
            metro_input.click()
            time.sleep(0.5)
            metro_input.clear()
            metro_input.send_keys(metro_station)
            time.sleep(1.5)
            
            for i in range(5):
                try:
                    station = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Order_Text')]")
                    if station.is_displayed():
                        station.click()
                        break
                except:
                    time.sleep(0.5)
            
            self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
            time.sleep(0.5)

    def click_next(self):
        with allure.step("Нажать Далее"):
            next_button = self.driver.find_element(*self.NEXT_BUTTON)
            next_button.click()
            time.sleep(3)
            self.wait_for_visibility(self.DELIVERY_DATE_INPUT)

    def fill_second_form(self, delivery_date, rental_period, color, comment):
        with allure.step(f"Заполнить вторую форму"):
            date_input = self.driver.find_element(*self.DELIVERY_DATE_INPUT)
            date_input.click()
            date_input.clear()
            date_input.send_keys(delivery_date)
            date_input.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
            dropdown = self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN)
            dropdown.click()
            time.sleep(0.5)
            period_option = self.driver.find_element(By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
            period_option.click()
            time.sleep(0.5)
            
            if color == "black":
                self.driver.find_element(*self.COLOR_BLACK).click()
            else:
                self.driver.find_element(*self.COLOR_GREY).click()
            time.sleep(0.5)
            
            self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
            time.sleep(0.5)

    def click_order_button(self):
        with allure.step("Нажать Заказать"):
            order_button = self.driver.find_element(*self.ORDER_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
            time.sleep(1)
            order_button.click()
            time.sleep(2)

    def confirm_order(self):
        with allure.step("Подтвердить заказ"):
            time.sleep(2)
            try:
                confirm_button = self.wait_for_clickable(self.CONFIRM_BUTTON)
                confirm_button.click()
            except:
                confirm_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Да']")
                confirm_button.click()
            time.sleep(3)

    def create_order(self, name, surname, address, metro_station, phone, 
                     delivery_date, rental_period, color, comment):
        self.fill_first_form(name, surname, address, metro_station, phone)
        self.click_next()
        self.fill_second_form(delivery_date, rental_period, color, comment)
        self.click_order_button()
        self.confirm_order()