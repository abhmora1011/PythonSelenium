import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# iframe, frameset , frame
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="../chromedriver")

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# Accept frame id, name or index value
driver.switch_to.frame("mce_0_ifr")

wait = WebDriverWait(driver, 10)

iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tinymce p")))

iframe.clear()
iframe.send_keys("I'm able to automate")

driver.switch_to.default_content() # Going back to normal HTML from iframe

print(driver.find_element(By.TAG_NAME, "h3").text)

time.sleep(2)

driver.quit() # close the session of the driver

