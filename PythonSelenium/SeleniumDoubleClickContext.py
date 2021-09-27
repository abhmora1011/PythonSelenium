import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

# driver.get("https://www.familysearch.org/en/")

#mouse_to_hover = driver.find_element(By.XPATH, "//nav[@id='primaryNav']/div[2]")

#action.move_to_element(mouse_to_hover).click().perform()

#action.move_to_element(driver.find_element(By.XPATH, "//ul[@id='search']/li/a[text()='Genealogies']")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

# NOTE ActionChains in python is heavily unstable [LIMIT PRACTICE ]

action = ActionChains(driver)

driver.maximize_window()

action.context_click(driver.find_element(By.ID, "double-click")).perform() # right click the element

action.double_click(driver.find_element(By.ID, "double-click")).perform()

alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()

time.sleep(2)

driver.quit() # close the session of the driver


