import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_first():
    """
    TK-235. Тест запуска браузера
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("stark-maximized") # open Browser in maximized mode 
    chrome_options.add_argument("--disable-infobars") # disable-infobars
    chrome_options.add_argument("--disable-extensions") # disable-extensions
    chrome_options.add_argument("--disable-gpu") # applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resour
    # chrome_options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service = service, options=chrome_options)
    driver.get(url="https://testqastudio.me/")

    assert True, ''



