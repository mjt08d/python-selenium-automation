#Part 1

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#E-mail field
driver.find_element(By.ID, 'ap_email')

#continue button
driver.find_element(By.ID, 'continue')

#conditions of use
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#provacy statement
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#forgot your password
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#other issues with sign-in
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


# Part 2

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

#click on signin button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()


#click on sign in on account page
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(6)

#Verify
actual_text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
assert 'Sign' in actual_text, f'Error text Sign not in {actual_text}'
print('test case passed')

driver.find_element(By.XPATH, "//button[@type='submit']")

driver.quit()