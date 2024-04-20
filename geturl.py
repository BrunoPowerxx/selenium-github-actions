from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from sb_page import SupabetsPageLocators
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

# Load the Supabets website
driver.get("https://supabets.co.za")

# Extract all the links from the page
links = driver.find_elements(By.TAG_NAME, 'a')

# Extract the href attribute from each link
urls = [link.get_attribute('href') for link in links]

# Filter out None values
urls = [url for url in urls if url]

# Print the extracted URLs
for url in urls:
    print(url)

# Close the WebDriver session
driver.quit()
