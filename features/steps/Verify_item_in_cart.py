from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SEARCH_WORD = "cups"
SEARCH_CUPS = (By.ID, 'search')
CLICK_SEARCH = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_ITEM = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor82242697")
ADD_TO_CART = (By.CSS_SELECTOR, "[aria-label*='Add to cart for Ball Aluminum']")
VIEW_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
VERIFY_CART = (By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan']")


@when('Click on the "Search" field and type in cups')
def click_on_search_field(context):
    context.driver.find_element(*SEARCH_CUPS).send_keys(SEARCH_WORD)
    context.driver.find_element(*CLICK_SEARCH).click()
    sleep(10)


@when('Click Add to cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_ITEM).click()
    sleep(10)


@when('Click on "Add to cart" button from "Choose options" drop down')
def click_on_add_to_cart_dropdown(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(10)


@when('Click on "View cart & check out" button on dropdown menu')
def click_on_view_cart_and_check_out(context):
    context.driver.find_element(*VIEW_CHECKOUT).click()
    sleep(10)


@then('Verify cups are in the cart')
def verify_cups_are_the_cart(context):
    context.driver.find_element(*VERIFY_CART)

