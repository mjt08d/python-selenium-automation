from pages.base_page import BasePage
from time import sleep

from selenium.webdriver.common.by import By

class Header(BasePage):
    SEARCH_CUPS = (By.ID, 'search')
    CLICK_SEARCH = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('cups', *self.SEARCH_CUPS)
        self.click(*self.CLICK_SEARCH)
        sleep(10)




