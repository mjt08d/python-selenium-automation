from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    VERIFY_CART = (
    By.XPATH, "//a[contains(@href, 'ball-aluminum-cup-recyclable-party-cups') and @data-test='cartItem-linked-title']")

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.VERIFY_CART).text
        assert expected_item in actual_text, f'Expected "{expected_item} in the cart" but got "{actual_text}"'

