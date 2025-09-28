# пустая строка в начале
import sys
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Добавляем корень проекта для корректного импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.mark.saucedemo
@allure.title("Покупка товара на SauceDemo")
@allure.feature("SauceDemo Purchase")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_purchase(driver: webdriver.Chrome):
    with allure.step("Открываем сайт SauceDemo"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизация"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Ожидание загрузки Products Page"):
        products_page = ProductsPage(driver)
        products_page.wait_for_page()

    with allure.step("Добавляем рюкзак в корзину"):
        products_page.add_backpack_to_cart()
        products_page.verify_backpack_added()

    with allure.step("Переходим в корзину"):
        products_page.go_to_cart()

    with allure.step("Проверяем, что рюкзак в корзине"):
        cart_page = CartPage(driver)
        cart_page.wait_for_page()
        item_name = cart_page.get_first_item_name()
        assert item_name == "Sauce Labs Backpack"
