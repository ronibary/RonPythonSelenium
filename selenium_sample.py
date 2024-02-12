from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# implicitly wait 5 seconds for all elements before throwing Exception
driver.implicitly_wait(5)

driver.get('http://www.gmail.com')
print(driver.title)
driver.quit()
