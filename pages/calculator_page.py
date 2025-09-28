# пустая строка в начале
# PR placeholder: ничего не меняем, просто для отображения изменений2
from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/"
         "slow-calculator.html"
         )

    def set_delay(self, delay: str):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, value: str):
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        )
        button.click()

    def get_result(self) -> str:
        return self.driver.find_element(*self.result_field).text
