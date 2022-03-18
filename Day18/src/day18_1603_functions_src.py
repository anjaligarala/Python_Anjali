import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def open_max_nav_chrome_browser():
    print(f"Open Chrome browser")
    driver = webdriver.Chrome()
    print(f"maximize the window of Chrome browser")
    driver.maximize_window()
    print(f"Navigating to the URL")
    driver.get("https://www.google.com/")
    print(f"Navigate till Google search text box and Enter value to search")
    driver.find_element(By.NAME, value='q').send_keys("javatpoint")
    print(f"Click on Enter")
    time.sleep(3)
    driver.find_element(By.NAME, value='btnK').send_keys(Keys.ENTER)
    print(f"Close the browser")
    driver.close()


open_max_nav_chrome_browser()
