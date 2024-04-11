from selenium import webdriver
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
odd_type_element = driver.find_element(By.CLASS_NAME, 'oddType')
odd_value_element = driver.find_element(By.CLASS_NAME, 'oddValue')

odd_type = odd_type_element.text
odd_value = odd_value_element.text

print("Odd Type:", odd_type)
print("Odd Value:", odd_value)

# Close the WebDriver
driver.quit()
