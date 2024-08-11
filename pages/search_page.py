import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class SearchPage(BasePage):
    popup_close_button = (By.XPATH, '//button[@aria-label="Close"]')
    streamer_info = (By.XPATH, '//h2/following-sibling::div//p')
    streamer_links_xpath = '//a[@href and contains(@href, "/videos/")]'

    def __init__(self, driver):
        super().__init__(driver)
    
    def select_random_streamer(self, scroll_times=2):
        self.scroll_down(scroll_times)
        streamer_elements = self.wait_for_all_elements(self.streamer_links_xpath)
        print(f"Found {len(streamer_elements)} streamer links.")
        random_streamer_element = random.choice(streamer_elements)
        video_href = random_streamer_element.get_attribute('href')
        print(f"Selected random video link: {video_href}")
        self.driver.get(video_href)
        self.wait_for_page_load()
        return random_streamer_element

    def handle_popup(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.popup_close_button))
            self.driver.find_element(self.popup_close_button).click()
            print("Popup closed")
        except Exception as e:
            print("No popup found or error closing popup")
