from selenium.webdriver.common.by import By
from behave import given, when
from time import sleep


SIGNIN_HOMEPAGE = (By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']")
DROPDOWN_SIGNIN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


@given('Open Target homepage')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click the "Sign in" button on upper right of homepage and click the "Sign in" button on drop down menu')
def click_signin(context):
    context.driver.find_element(*SIGNIN_HOMEPAGE).click()
    context.driver.find_element(*DROPDOWN_SIGNIN).click()
    sleep(3)


@when('Click on "Cart" icon')
def click_on_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)