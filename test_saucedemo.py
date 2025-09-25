# внесение изменений
# flake8: noqa: E402
# Добавляем корень проекта в sys.path для корректного импорта
import sys
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импорт PageObject
from pages.login_page import LoginPage


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
@allure.description(
    "Тест проверяет, что пользователь может добавить рюкзак в корзину и проверить его наличие"
)
@allure.feature("SauceDemo Purchase")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_purchase(driver: webdriver.Chrome) -> None:
    with allure.step("Открываем сайт SauceDemo"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Ждём загрузки страницы инвентаря"):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "inventory_list"))
        )

    with allure.step("Добавляем рюкзак в корзину"):
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

    with allure.step("Проверяем, что товар добавлен в корзину"):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
        )

    with allure.step("Переходим в корзину"):
        cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

    with allure.step("Ждём открытия страницы корзины"):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

    with allure.step("Проверяем наличие товара в корзине"):
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert cart_item.text == "Sauce Labs Backpack"
