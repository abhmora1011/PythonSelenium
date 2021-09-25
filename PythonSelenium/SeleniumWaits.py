import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

list_item = []
summary_item = []

driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

time.sleep(4)

count_of_result = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))

assert count_of_result == 3

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for btn in buttons:
    list_item.append(btn.find_element(By.XPATH, "parent::div/parent::div/h4").text) # connection xpath by traversing back
    btn.click()

to_cart = driver.find_elements(By.XPATH, "//h4[@class='product-name']")

print(list_item)

driver.find_element(By.XPATH, "//div[@class='cart']/a[4]").click()

driver.find_element(By.XPATH, "//div[@class='cart']/div[2]/div/button").click()

wait = WebDriverWait(driver, 10)

input_code = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='promoWrapper']/input")))

to_summary = driver.find_elements(By.CSS_SELECTOR, "p.product-name")

for summary in to_summary:
    summary_item.append(summary.text)

print(summary_item)

'''SAMPLE  FETCHING AMOUNT'''
total_amounts = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(5)")

total = 0
for t_amount in total_amounts:
    total += int(t_amount.text)

print("{} {}".format("This is the total amount", total))
'''END OF SAMPLE FETCHING'''

original_amount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
print(original_amount)

input_code.send_keys("rahulshettyacademy")

btn_code = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='promoWrapper']/button")))

btn_code.click()

promo_applied_msg = wait.until((EC.presence_of_element_located((By.XPATH, "//div[@class='promoWrapper']/span"))))

# print(promo_applied_msg.text)
discount_amount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
print(discount_amount)

assert list_item == summary_item

assert int(original_amount) == total

assert float(discount_amount) < float(original_amount)

assert "Code applied ..!" in promo_applied_msg.text



time.sleep(2)

driver.quit()

