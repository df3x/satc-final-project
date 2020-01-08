from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINKS = (By.CSS_SELECTOR, ".header a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_PRODUCT_SET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form [type='submit']")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info div p:nth-child(1) strong")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) div strong")
