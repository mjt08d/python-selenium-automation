# PART 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Click cart icon
driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

sleep(6)

# Verify cart empty
actual_text = driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem").text
assert "empty" in actual_text, f'Error text empty not in {actual_text}'
print('test case passed')


