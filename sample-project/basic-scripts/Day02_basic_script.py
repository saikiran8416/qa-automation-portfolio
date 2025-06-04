from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://app.vwo.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

