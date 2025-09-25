# PR placeholder: ничего не меняем, просто для отображения изменений2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name):
        # Ждём, пока элемент товара будет виден
        product_locator = (
            By.XPATH,
            (
                f"//div[@class='inventory_item' and "
                f".//div[text()='{product_name}']]"
             )
        )
        self.wait.until(EC.visibility_of_element_located(product_locator))

        # Находим кнопку "Add to cart" внутри этого блока
        button_locator = (
            By.XPATH,
            (
                f"//div[@class='inventory_item' and "
                f".//div[text()='{product_name}']]//button"
             )
        )
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        button.click()

    def go_to_cart(self):
        cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        cart_button = self.wait.until(EC.element_to_be_clickable(cart_locator))
        cart_button.click()
