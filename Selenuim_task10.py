from selenium import webdriver #import webdriver module to control web browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Import By class to locate elements using different locator strategies
from selenium.webdriver.chrome.service import Service ## Import Service class to manage ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager ## Import ChromeDriverManager to automatically download and manage ChromeDriver
import time ## Import time module to add static wait (sleep)

def selenium_task10(): #function
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #launch chrome browser
    driver.maximize_window() #maximize window for better visibility

    driver.get("https://www.saucedemo.com/") #launch sauce demo app

    #Enter login details
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click() #click on login button

    time.sleep(8) #wait to load page completely

    title = driver.title  #captures title of current url
    current_url = driver.current_url #captures current url
    print("Tile:", title)
    print("URL:", current_url)

    page_contents = driver.page_source  #get complete html source of current webpage
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file: #create text file and write webpage html content
        file.write(page_contents)

    driver.quit() #close browser


if __name__ == "__main__": ## Entry point of the Python script Ensures the function runs only when the file is executed directly, not when imported
    selenium_task10()

