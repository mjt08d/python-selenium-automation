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


