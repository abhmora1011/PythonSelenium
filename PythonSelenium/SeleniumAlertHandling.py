import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

validateTxt = "Option3"

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateTxt)

driver.find_element(By.ID, "confirmbtn").click()

# To handle a Java Alert Popup
alert = driver.switch_to.alert

print(alert.text)

assert validateTxt in alert.text

alert.accept() # select OK/CONFIRM btn in the alert pop up
# alert.dismiss() # select CANCEL btn in the alert pop up

# if alert has a [CANCEL] [CONFIRM] btn
# use alert.accept() and alert.dismiss()

time.sleep(3)

driver.quit()


