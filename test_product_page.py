from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

MAIN_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket_with_promo(browser, promo_offer):
    link = f"{MAIN_LINK}?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = MAIN_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_product_added_to_basket()

@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = MAIN_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
#Открываем страницу товара
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = MAIN_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = MAIN_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_appeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    LoginPage(browser, None).should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#Гость открывает страницу товара
#Переходит в корзину по кнопке в шапке
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    BasketPage(browser, None).should_be_basket_page_is_empty()

@pytest.mark.logon_user
class TestUserAddToBasketFromProductPage:
    #ВАЖНО! Манипулировать браузером в сетапе и уж тем более что-то там проверять — это плохая практика,
    #пример в учебных целях!
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Здесь хорошо работать по апи
        link = MAIN_LINK
        login = LoginPage(browser, link)
        login.open()
        login.go_to_login_page()
        self.login = login
        tmp = str(time.time())
        email = tmp + "@fakemail.org"
        pas = "qW" + tmp
        login.register_new_user(email, pas)
        login.should_be_authorized_user()
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        # to-do: self.login.delete()
        pass

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = MAIN_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_product_added_to_basket()

    def test_user_cant_see_success_message(self, browser):
        link = MAIN_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()