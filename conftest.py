import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    # Путь к geckodriver
    geckodriver_path = r'C:\Users\daniy\Documents\geckodriver-v0.36.0-win32\geckodriver.exe'
    
    # Путь к Firefox (добавлен .exe в конце)
    firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    
    # Настройки Firefox
    options = Options()
    options.binary_location = firefox_path
    
    # Запуск браузера
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)
    
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"