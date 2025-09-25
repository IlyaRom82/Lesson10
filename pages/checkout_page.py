# PR placeholder: ничего не меняем, просто для отображения изменений2
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        (self.driver.find_element
         (*self.postal_code_input).send_keys(postal_code)
         )

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.total_label).text
        # Возвращаем только цифры, например $58.29 -> 58.29
        return float(total_text.replace("Total: $", ""))
