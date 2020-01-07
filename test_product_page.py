from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.skip()
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket()

@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
#Открываем страницу товара
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_appeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    LoginPage(browser, None).should_be_login_page()