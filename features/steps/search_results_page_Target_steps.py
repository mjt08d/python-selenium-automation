from selenium.webdriver.common.by import By
from behave import then



SIGNIN_TEXT = (By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']")


@then('Verify "Sign in" page opens')
def verify_signin(context):
    actual_text = context.driver.find_element(*SIGNIN_TEXT).text
    assert 'Sign' in actual_text, f'Error text Sign not in {actual_text}'


