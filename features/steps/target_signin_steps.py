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
