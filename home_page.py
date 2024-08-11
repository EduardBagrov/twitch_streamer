from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.search_label = (By.XPATH, "//a[@aria-label='Search']")
        self.search_input = (By.XPATH, "//input[@type='search']")
        self.view_all_videos = (By.XPATH, '//div[text()="Videos"]')

    def open(self):
        self.driver.get("https://m.twitch.tv/")

    def click_search_label(self):
        try:
            search_label_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_label)
            )
            search_label_element.click()
        except Exception as e:
            print(f"Error locating a search input: {e}")

    def enter_search_text(self, text):
        try:
            search_input_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_input_element.clear()
            search_input_element.send_keys(text)
            search_input_element.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error searching text: {e}")

    def click_view_all_videos(self):
        try:
            view_all_videos = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.view_all_videos)
            )
            view_all_videos.click()
        except Exception as e:
            print(f"Error clicking 'Videos' tab: {e}")
