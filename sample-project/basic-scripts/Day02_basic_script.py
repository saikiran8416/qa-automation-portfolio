from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://app.vwo.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
