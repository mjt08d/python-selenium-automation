from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LINKS = (By.CSS_SELECTOR, "[data-lnk='Join Circle '],[data-lnk='Circle Deals '],[data-lnk='Bonus'],[data-lnk='Partner'],[data-lnk='Voting '],[data-lnk='Circe FAQs']")

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify 6 links are present on "Circle Page"')
def verify_navigation_bar(context):
    links = context.driver.find_elements(*LINKS)
    print(links)
    assert len(links) == 6, f'Expected 6 links but got {len(links)}'