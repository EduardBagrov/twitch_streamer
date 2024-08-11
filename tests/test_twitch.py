import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium import webdriver

from pages.popup_page import PopupPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://m.twitch.tv")
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def search_page(driver):
    return SearchPage(driver)


def test_search_for_streamer(home_page, search_page):
    home_page.click_search_label()
    keyword = "StarCraft II"
    home_page.enter_search_text(keyword)
    home_page.click_videos_tab()
    streamer = search_page.select_random_streamer()
    assert streamer is not None, "Expected to find streamers in the search results."
    search_page.take_screenshot("search_result.png")
