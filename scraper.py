from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas
import csv

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('http://supabets.co.za')
#driver.get('http://supabets.co.za')

# Find all elements with class name 'oddType'
odd_type_elements = driver.find_elements(By.CLASS_NAME, 'oddType')
# Find all elements with class name 'oddValue'
odd_value_elements = driver.find_elements(By.CLASS_NAME, 'oddValue')

# Iterate through each pair of elements and print their text
for odd_type_element, odd_value_element in zip(odd_type_elements, odd_value_elements):
    odd_type = odd_type_element.text
    odd_value = odd_value_element.text
    print("Odd Type:", odd_type)
    print("Odd Value:", odd_value)

# Close the WebDriver
# driver.quit()


# Close the WebDriver
driver.quit()
