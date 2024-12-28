from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver
