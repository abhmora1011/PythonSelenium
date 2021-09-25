import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver")

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.PARTIAL_LINK_TEXT, "Click Here").click()

# 0 index is assigned to Parent || This code is responsible in getting the window
driver.window_handles # Fetch the list of windows
child_window = driver.window_handles[1]

# Switch to window to another by passing the ID
driver.switch_to.window(child_window)

driver.close() # close the current active window

print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

driver.quit() # close the session of the driver

