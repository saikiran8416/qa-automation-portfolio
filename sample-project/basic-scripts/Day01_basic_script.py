# selecting object from webpage using product name.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#add item to the cart
def add_item(item):
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    itemslist = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for item in itemslist:
        productname = item.find_element(By.XPATH, "div/h4/a").text
        if productname == item:
            item.find_element(By.XPATH, "div/button").click()

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
add_item("Blackberry")
#move to checkout page
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
exwait=WebDriverWait(driver,10)
exwait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successtext= driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success" in successtext

time.sleep(30)

driver.close()