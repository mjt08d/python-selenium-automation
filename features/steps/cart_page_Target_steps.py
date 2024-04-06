from selenium.webdriver.common.by import By
from behave import then


CART_EMPTY_TEXT = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem")


@then('Verify "Your cart is empty" text is shown')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(*CART_EMPTY_TEXT).text
    assert "empty" in actual_text, f'Error text empty not in {actual_text}'