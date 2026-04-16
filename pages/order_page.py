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
                    print("✅ Куки закрыты")
                    time.sleep(0.5)
            except:
                print("ℹ️ Куки нет")

    def fill_first_form(self, name, surname, address, metro_station, phone):
        with allure.step(f"Заполнить первую форму"):
            self.close_cookie_banner()
            
            name_input = self.wait_for_visibility(self.NAME_INPUT)
            name_input.send_keys(name)
            print(f"✅ Имя: {name}")
            time.sleep(0.3)
            
            surname_input = self.driver.find_element(*self.SURNAME_INPUT)
            surname_input.send_keys(surname)
            print(f"✅ Фамилия: {surname}")
            time.sleep(0.3)
            
            address_input = self.driver.find_element(*self.ADDRESS_INPUT)
            address_input.send_keys(address)
            print(f"✅ Адрес: {address}")
            time.sleep(0.3)
            
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
            
            print(f"✅ Станция: {metro_station}")
            time.sleep(0.5)
            
            phone_input = self.driver.find_element(*self.PHONE_INPUT)
            phone_input.send_keys(phone)
            print(f"✅ Телефон: {phone}")
            time.sleep(0.5)
            
            print("✅ Первая форма заполнена")

    def click_next(self):
        with allure.step("Нажать Далее"):
            next_button = self.driver.find_element(*self.NEXT_BUTTON)
            next_button.click()
            print("🔘 Нажата кнопка 'Далее'")
            time.sleep(3)
            self.wait_for_visibility(self.DELIVERY_DATE_INPUT)
            print("✅ Вторая форма открылась")

    def fill_second_form(self, delivery_date, rental_period, color, comment):
        with allure.step(f"Заполнить вторую форму"):
            date_input = self.driver.find_element(*self.DELIVERY_DATE_INPUT)
            date_input.click()
            date_input.clear()
            date_input.send_keys(delivery_date)
            date_input.send_keys(Keys.ENTER)
            print(f"✅ Дата: {delivery_date}")
            time.sleep(0.5)
            
            dropdown = self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN)
            dropdown.click()
            time.sleep(0.5)
            period_option = self.driver.find_element(By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
            period_option.click()
            print(f"✅ Период: {rental_period}")
            time.sleep(0.5)
            
            if color == "black":
                color_checkbox = self.driver.find_element(*self.COLOR_BLACK)
                color_checkbox.click()
                print("✅ Цвет: черный жемчуг")
            else:
                color_checkbox = self.driver.find_element(*self.COLOR_GREY)
                color_checkbox.click()
                print("✅ Цвет: серая безысходность")
            time.sleep(0.5)
            
            comment_input = self.driver.find_element(*self.COMMENT_INPUT)
            comment_input.send_keys(comment)
            print(f"✅ Комментарий: {comment}")
            time.sleep(0.5)
            
            print("✅ Вторая форма заполнена")

    def click_order(self):
        with allure.step("Нажать Заказать"):
            time.sleep(1)
            # Кнопка "Заказать" в том же контейнере, что и "Назад"
            order_button = self.driver.find_element(By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
            
            self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
            time.sleep(1)
            order_button.click()
            print("🔘 Нажата кнопка 'Заказать'")
            time.sleep(2)

    def confirm_order(self):
        with allure.step("Подтвердить заказ"):
            time.sleep(2)
            try:
                confirm_button = self.wait_for_clickable(self.CONFIRM_BUTTON)
                confirm_button.click()
                print("🔘 Нажата кнопка 'Да'")
            except:
                try:
                    confirm_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Да']")
                    confirm_button.click()
                    print("🔘 Нажата кнопка 'Да'")
                except:
                    print("❌ Кнопка 'Да' не найдена!")
            time.sleep(3)

    def create_order(self, name, surname, address, metro_station, phone, 
                     delivery_date, rental_period, color, comment):
        print("\n" + "="*50)
        print("🚀 НАЧАЛО ЗАКАЗА")
        print("="*50)
        self.fill_first_form(name, surname, address, metro_station, phone)
        self.click_next()
        self.fill_second_form(delivery_date, rental_period, color, comment)
        self.click_order()
        self.confirm_order()
        print("\n" + "="*50)
        print("✅ ЗАКАЗ СОЗДАН!")
        print("="*50)