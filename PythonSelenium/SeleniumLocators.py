from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Locators
# ID
# Name
''' Xpath -> REGEX //*[contains(@attribute,'value')], 
                   //tagname[@attribute="value"]  *** tag name is optional *** '''

''' Generating XPATH based on text
                  //tagname[text()='xxx'] (Can cover any tag) '''

''' Creating Xpath and CSS by Traversing Tags
            xpath: ParentTag/ChildTag
            CSS: ParentTag ChildTag '''

''' CSS -> REGEX: [attribute*='value']
           tagname[attribute='value'] *** tag name is optional ***'''

''' Generating CSS from ID
           tagname#ID || tagname.CLASSNAME'''

# ClassName
# linkText
# TagName


driver = webdriver.Chrome(executable_path="/Users/hnstabe/Documents/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Abraham")  # NAME

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("aora@gmail.com")  # CSS_SELECTOR

driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("12345")  # XPATH

driver.find_element(By.ID, "exampleCheck1").click()  # ID

driver.find_element(By.XPATH, "//input[@type='submit']").click()

print(driver.find_element(By.CLASS_NAME, "alert-success").text)
# $("[class*='alert-success']") CSS REGEX Console Checking
# $("[class='alert-success'") CSS Console Checking
# $x("//*[contains(@class,'alert-success')]") XPATH REGEX Console Checking
# $x("//div[@class='alert-success']") XPATH Console Checking


# driver.close()
