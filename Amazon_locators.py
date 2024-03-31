# PART 1

# Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# Create Account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Your Name Field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.auth-autofocus.auth-required-field")

# Mobile number or EMAIL field
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# Password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

# Re-enter password
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

# Continue button
driver.find_element(By.CSS_SELECTOR, "input#continue")

# Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use?']")

# Privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice?']")

# Already have an account "Sign In" button
driver.find_elemeent(By.CSS_SELECTOR, "a.a-link-emphasis")