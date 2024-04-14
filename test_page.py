# import dependencies

import pytest
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

#testlogic

def test_scrape_odd_info(driver):
    driver.get(SupabetsPageLocators.URL)

    sport_name_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.SPORT_NAME_SELECTOR)
    league_name_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.LEAGUE_NAME_SELECTOR)
    home_team_name_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.HOME_TEAM_NAME_SELECTOR)
    away_team_name_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.AWAY_TEAM_NAME_SELECTOR)
    market_type_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.MARKET_TYPE_SELECTOR)
    odd_type_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.ODD_TYPE_SELECTOR)
    odd_value_element = driver.find_element(By.CSS_SELECTOR, SupabetsPageLocators.ODD_VALUE_SELECTOR)

    sport_name = sport_name_element.text
    league_name = league_name_element.text
    home_team_name = home_team_name_element.text
    away_team_name = away_team_name_element.text
    market_type = market_type_element.text
    odd_type = odd_type_element.text
    odd_value = odd_value_element.text


    print("Sport:", sport_name)
    print("League:", league_name)
    print("Home:", home_team_name)
    print("Away:", away_team_name)
    print("Market:", market_type)
    print("Odd Type:", odd_type)
    print("Odd Value:", odd_value)
    print(" ")
