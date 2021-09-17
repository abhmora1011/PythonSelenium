from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.get("https://login.salesforce.com/?locale=ap")

driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Hello")

driver.find_element(By.CSS_SELECTOR, ".password").send_keys("World")

driver.find_element(By.CSS_SELECTOR, ".password").clear()

print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] div[id='usernamegroup'] label").text)

driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot ").click()

driver.find_element(By.XPATH, "//input[@value='Cancel']").click()


