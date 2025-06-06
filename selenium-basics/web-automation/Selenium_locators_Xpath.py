from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Make')]")
    make_app_btn.click()
    time.sleep(5)
    driver.quit()  # close everything.
