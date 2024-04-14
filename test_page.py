# import dependencies

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sb_page import SupabetsPageLocators

# pytest + chrome logic
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.quit()

#testlogic

def test_scrape_odd_info(browser):
    browser.get(SupabetsPageLocators.URL)

    sport_name_element = browser.find_element_by_css_selector(SupabetsPageLocators.SPORT_NAME_SELECTOR)
    league_name_element = browser.find_element_by_css_selector(SupabetsPageLocators.LEAGUE_NAME_SELECTOR)
    home_team_name_element = browser.find_element_by_css_selector(SupabetsPageLocators.HOME_TEAM_NAME_SELECTOR)
    away_team_name_element = browser.find_element_by_css_selector(SupabetsPageLocators.AWAY_TEAM_NAME_SELECTOR)
    market_type_element = browser.find_element_by_css_selector(SupabetsPageLocators.MARKET_TYPE_SELECTOR)
    odd_type_element = browser.find_element_by_css_selector(SupabetsPageLocators.ODD_TYPE_SELECTOR)
    odd_value_element = browser.find_element_by_css_selector(SupabetsPageLocators.ODD_VALUE_SELECTOR)

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