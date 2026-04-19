import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
from urls import Urls

load_dotenv()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    firefox_path = os.getenv("FIREFOX_PATH")
    if firefox_path:
        options.binary_location = firefox_path
    
    geckodriver_path = os.getenv("GECKODRIVER_PATH")
    
    if geckodriver_path:
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
    else:
        driver = webdriver.Firefox(options=options)
    
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    
    yield driver
    
    driver.quit()