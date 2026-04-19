from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


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
    
    # Локатор для станции метро в выпадающем списке
    STATION_OPTION = (By.XPATH, "//div[contains(@class, 'Order_Text')]")

    @allure.step("Закрыть куки-баннер")
    def close_cookie_banner(self):
        try:
            close_button = self.driver.find_element(*self.COOKIE_CLOSE_BUTTON)
            if close_button.is_displayed():
                close_button.click()
        except:
            pass

    @allure.step("Заполнить первую форму")
    def fill_first_form(self, name, surname, address, metro_station, phone):
        self.close_cookie_banner()
        
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        metro_input = self.find_element(self.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        
        # Явное ожидание появления списка станций
        self.wait.until(EC.visibility_of_element_located(self.STATION_OPTION))
        station = self.find_element(self.STATION_OPTION)
        station.click()
        
        self.send_keys(self.PHONE_INPUT, phone)

    @allure.step("Нажать Далее")
    def click_next(self):
        next_button = self.find_element(self.NEXT_BUTTON)
        next_button.click()
        self.wait.until(EC.visibility_of_element_located(self.DELIVERY_DATE_INPUT))

    @allure.step("Заполнить вторую форму")
    def fill_second_form(self, delivery_date, rental_period, color, comment):
        # Дата
        date_input = self.find_element(self.DELIVERY_DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)
        
        # Период аренды
        dropdown = self.find_element(self.RENTAL_PERIOD_DROPDOWN)
        dropdown.click()
        period_option = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
        self.wait.until(EC.element_to_be_clickable(period_option)).click()
        
        # Цвет
        if color == "black":
            self.find_element(self.COLOR_BLACK).click()
        else:
            self.find_element(self.COLOR_GREY).click()
        
        # Комментарий
        self.send_keys(self.COMMENT_INPUT, comment)

    @allure.step("Нажать Заказать")
    def click_order_button(self):
        order_button = self.find_element(self.ORDER_BUTTON)
        self.scroll_to_element(order_button)
        order_button.click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        confirm_button.click()

    @allure.step("Создать заказ")
    def create_order(self, name, surname, address, metro_station, phone, 
                     delivery_date, rental_period, color, comment):
        self.fill_first_form(name, surname, address, metro_station, phone)
        self.click_next()
        self.fill_second_form(delivery_date, rental_period, color, comment)
        self.click_order_button()
        self.confirm_order()