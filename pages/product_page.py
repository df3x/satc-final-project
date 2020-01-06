from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.product_name = self.get_product_name()
        self.product_price = self.get_product_price()
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn.click()

    def should_be_product_added_to_basket(self):
        self.should_be_product_name_correct(self.product_name)
        self.should_be_product_price_correct(self.product_price)

    def should_be_product_price_correct(self, product_price):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, f"Product price in basket '{product_price_in_basket}' is not equal '{product_price}'"

    def should_be_product_name_correct(self, product_name):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, f"Product name in basket '{product_name_in_basket}' is not equal '{product_name}'"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

