import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time

TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_clickable(self, by_locator, timeout=TIMEOUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            return element
        except Exception as e:
            print(f"Error locating a {by_locator}: {e}")

    
    def wait_element_presence(self, by_locator, timeout=TIMEOUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            return element
        except Exception as e:
            print(f"Error locating a {by_locator}: {e}")

    def wait_for_all_elements(self, by_locator, timeout=TIMEOUT):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, by_locator))
            )
            return elements
        except Exception as e:
            print(f"Error locating a {by_locator}: {e}")

    def click(self, by_locator):
        self.wait_element_clickable(by_locator).click()

    def enter_text(self, by_locator, text):
        element = self.wait_element_presence(by_locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def scroll_down(self, times):
        actions = ActionChains(self.driver)
        for i in range(times):
            print(f"Scrolling down: {i + 1}/{times}")
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(3)
            self.wait_for_page_load()

    def take_screenshot(self, file_name):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        file_path = os.path.join(screenshots_dir, file_name)
        self.driver.save_screenshot(file_path)

    def wait_for_page_load(self, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
