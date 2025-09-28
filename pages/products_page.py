# пустая строка в начале
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.backpack_remove_button = (By.ID, "remove-sauce-labs-backpack")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def wait_for_page(self):
        """Ожидаем загрузку списка товаров"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.inventory_list)
        )

    def add_backpack_to_cart(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_button)
        )
        button.click()

    def verify_backpack_added(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.backpack_remove_button)
        )

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
