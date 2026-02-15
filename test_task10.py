import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Test Case 1: Verify Homepage Title
# Purpose: Validate that the application loads with correct title - Positive
def test_homepage_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Launch Chrome browser
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/") #open Sauce deo app
    assert driver.title == "Swag Labs" #validate page title

    driver.quit() # close browser

# Test Case 2: Verify Homepage URL
# Purpose: Ensure user lands on correct URL before login - Positive
def test_homepage_url():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Launch Chrome Browser
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/" #validate homepage URL

    driver.quit() # Close Browser

# Test Case 3: Positive Login Test
# Purpose: Validate successful login with valid credentials - Positive
def test_pos_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Launch Chrome browser
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/") #launch Sauce demo app
    #Enter valid Login Details
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click() #click on login button

    time.sleep(4)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html" #validate dashboard URL after login

    driver.quit() #Close Browser

# Test Case 4: Invalid Login Test
# Purpose: Validate error message for incorrect credentials - Negative
def test_invalid_id():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #launch chrome browser
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/") # launch sauce demo app
    # Enter login details
    driver.find_element(By.ID, "user-name").send_keys("standard")
    driver.find_element(By.ID, "password").send_keys("secre")
    driver.find_element(By.ID, "login-button").click() #click on login button

    time.sleep(4)

    error = driver.find_element(By.XPATH, "//h3").text #validates error message
    assert "Epic sadface" in error

    driver.quit() #close browser

# Test Case 5: Empty Credentials Test
# Purpose: Validate system behavior when no credentials are provided - Negative
def test_empty_id():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #launch chrome browser
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/") #launch Sauce demo app
    driver.find_element(By.ID, "login-button").click() #direct click on login button

    error = driver.find_element(By.XPATH, "//h3").text #Validate required field error
    assert "Epic sadface" in error

    driver.quit()

