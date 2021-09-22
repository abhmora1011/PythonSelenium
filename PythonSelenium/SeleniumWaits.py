import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

time.sleep(4)

count_of_result = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))

assert count_of_result == 3

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for btn in buttons:
    btn.click()

driver.find_element(By.XPATH, "//div[@class='cart']/a[4]").click()

driver.find_element(By.XPATH, "//div[@class='cart']/div[2]/div/button").click()

wait = WebDriverWait(driver, 10)

input_code = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='promoWrapper']/input")))

input_code.send_keys("rahulshettyacademy")

btn_code = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='promoWrapper']/button")))

btn_code.click()

promo_applied_msg = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@class='promoWrapper']/span"))))

print(promo_applied_msg.text)

assert "Code applied ..!" in promo_applied_msg.text

time.sleep(2)

driver.quit()

