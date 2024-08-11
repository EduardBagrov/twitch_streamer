import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.popup_close_button = (By.XPATH, '//button[@aria-label="Close"]')
        self.streamer_info = (By.XPATH, '//h2/following-sibling::div//p')
        self.streamer_links_xpath = '//a[@href and contains(@href, "/videos/")]'

    def scroll_down(self):
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.streamer_links_xpath))
            )
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def select_random_streamer(self):
        try:
            streamer_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.streamer_links_xpath))
            )
            print(f"Found {len(streamer_elements)} streamer links.")

            random_streamer_element = random.choice(streamer_elements)
            video_href = random_streamer_element.get_attribute('href')
            print(f"Selected random video link: {video_href}")

            self.driver.get(video_href)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//video'))
            )
        except Exception as e:
            print(f"Error selecting streamer: {e}")

    def take_screenshot(self, file_location):
        self.driver.save_screenshot(file_location)

    def handle_popup(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.popup_close_button))
            self.driver.find_element(self.popup_close_button).click()
            print("Popup closed")
        except Exception as e:
            print("No popup found or error closing popup")
