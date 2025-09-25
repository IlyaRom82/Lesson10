# Добавляем корень проекта в sys.path для корректного импорта
import sys
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Добавляем корень проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Абсолютный импорт через пакет проекта
# flake8: noqa: E402
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Проверка сложения с задержкой")
@allure.description(
    "Тест проверяет работу калькулятора при сложении 7 + 8 "
    "с задержкой 45 секунд"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_addition_with_delay(driver: webdriver.Chrome) -> None:
    calc = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Установить задержку 45 секунд"):
        calc.set_delay("45")

    with allure.step("Нажать 7 + 8 ="):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")

    with allure.step("Дождаться появления результата '15' на экране"):
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

    with allure.step("Проверка результата"):
        result = calc.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
