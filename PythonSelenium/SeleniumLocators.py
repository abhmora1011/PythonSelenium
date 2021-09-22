from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import getAttribute_js

# Locators
# ID
# Name
from selenium.webdriver.support.select import Select

''' Xpath -> REGEX //*[contains(@attribute,'value')], 
                   //tagname[@attribute="value"]  *** tag name is optional *** '''

''' Generating XPATH based on text
                  //*[contains(text(),'xxx')] (Can cover any tag) 
                  //tagname[text()='<text here>']           '''

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

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)

driver.find_element(By.ID, "exampleCheck1").click()  # ID

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
# $("[class*='alert-success']") CSS REGEX Console Checking
# $("[class='alert-success'") CSS Console Checking
# $x("//*[contains(@class,'alert-success')]") XPATH REGEX Console Checking
# $x("//div[@class='alert-success']") XPATH Console Checking

assert "Success" in message # Check if present
# assert "Success" == message -> Check the exact message

# driver.close()
