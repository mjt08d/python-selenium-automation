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








