# пустая строка в начале
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cart_title = (By.CLASS_NAME, "title")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    def wait_for_page(self):
        """Ожидаем загрузку страницы корзины"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_title)
        )

    def get_first_item_name(self) -> str:
        """Возвращает имя первого товара в корзине"""
        return self.driver.find_element(*self.cart_item_name).text
