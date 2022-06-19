# imports
from selenium import webdriver

driver = webdriver.Firefox(
    executable_path=r'C:\Users\tobi1\OneDrive\S2 Uni Mannheim\Artificial Intelligence in Industrial Applications\Selenium_TS\geckodriver.exe')

driver.get('https://github.com')
# https://github.com/mozilla/geckodriver/releases