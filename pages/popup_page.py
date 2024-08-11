# pages/popup_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PopupPage(BasePage):

    popup_close_locator = (By.XPATH, '//button[@aria-label="Close"]')

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        try:
            self.wait_element_presence(self.popup_close_locator).click()
            print("Popup closed")
        except Exception as e:
            print("No popup found or error closing popup")

