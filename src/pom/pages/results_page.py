from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePageElement


class ResultsPage(BasePageElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_BOX = (By.XPATH, "//input[contains(@class,'nav-search-input')]")
    RESULTS_CARDS = (By.CLASS_NAME, "ui-search-result__wrapper")
    PRODUCT_TITLE = (By.CLASS_NAME, "ui-search-item__group--title")

    def get_products_list_title_text(self):
        elements = self.find_multiple_elements(self.PRODUCT_TITLE)
        return [element.get_attribute("innerText") or "" for element in elements]

    def search_product_in_list(self, search_term, minimum_match_ratio=0.5):
        product_titles = self.get_products_list_title_text()
        if not product_titles:
            return False

        matching_titles = sum(
            search_term.casefold() in title.casefold()
            for title in product_titles
        )
        return matching_titles / len(product_titles) >= minimum_match_ratio
