# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    search_label = (By.XPATH, "//a[@aria-label='Search']")
    search_input = (By.XPATH, "//input[@type='search']")
    view_all_videos = (By.XPATH, '//div[text()="Videos"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_label(self):
        self.click(self.search_label)

    def enter_search_text(self, text):
        self.enter_text(self.search_input, text)

    def click_videos_tab(self):
        self.click(self.view_all_videos)