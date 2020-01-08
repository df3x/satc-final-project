from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page_is_empty(self):
        self.should_be_basket_url()
        self.should_be_empty_basket()
        self.should_not_be_product_in_basket()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url is not correct"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket should be empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_SET), \
               "Basket has set product, but should not be"
