from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH_WORD = "cups"
SEARCH_CUPS = (By.ID, 'search')
CLICK_SEARCH = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_ITEM = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor82242697")
ADD_TO_CART = (By.CSS_SELECTOR, "[aria-label*='Add to cart for Ball Aluminum']")
VIEW_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
VERIFY_CART = (By.XPATH, "//a[contains(@href, 'ball-aluminum-cup-recyclable-party-cups') and @data-test='cartItem-linked-title']")


@when('Click on the "Search" field and type in cups')
def click_on_search_field(context):
    # context.driver.find_element(*SEARCH_CUPS).send_keys(SEARCH_WORD)
    # context.driver.find_element(*CLICK_SEARCH).click()
    # sleep(10)
    context.app.header.search_product()


@when('Click Add to cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_ITEM).click()
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(ADD_TO_CART))


@when('Click on "Add to cart" button from "Choose options" drop down')
def click_on_add_to_cart_dropdown(context):
    context.driver.find_element(*ADD_TO_CART).click()
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.element_to_be_clickable(VIEW_CHECKOUT))


@when('Click on "View cart & check out" button on dropdown menu')
def click_on_view_cart_and_check_out(context):
    context.driver.find_element(*VIEW_CHECKOUT).click()


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    # actual_text = context.driver.find_element(*VERIFY_CART).text
    # assert expected_item in actual_text, f'Expected "{expected_item} in the cart" but got "{actual_text}"'
    context.app.search_results_page.verify_search_results(expected_item)




