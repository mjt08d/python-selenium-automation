# ************************PART 1**************************

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

# *******************PART 2*********************************

# *******************TARGET CART TESTS*********************

# Created by michaeltrisotto at 3/31/24
Feature: "Your cart is empty" text verification


  Scenario: Verity user can see "Your cart is empty" on "Cart" page
    Given Open Target homepage
    When Click on "Cart" icon
    Then Verify "Your cart is empty" text is shown

# ********************TARGET CART STEPS**********************

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target homepage')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click on "Cart" icon')
def click_on_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(6)

@then('Verify "Your cart is empty" text is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem").text
    assert "empty" in actual_text, f'Error text empty not in {actual_text}'


#********************PART3*******************************

# *****************TARGET SIGH IN TESTS******************

# Created by michaeltrisotto at 3/31/24
Feature: Sign in verification


  Scenario: Verify user can sign in once logged out
    Given Open Target homepage
    When Click the "Sign in" button on upper right of homepage and click the "Sign in" button on drop down menu
    Then Verify "Sign in" page opens

# ******************TARGET SIGN IN STEPS*****************************

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target homepage')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click the "Sign in" button on upper right of homepage and click the "Sign in" button on drop down menu')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(6)

@then('Verify "Sign in" page opens')
def verify_signin(context):
    actual_text = context.driver.find_element(By.XPATH,
    "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
    assert 'Sign' in actual_text, f'Error text Sign not in {actual_text}'
