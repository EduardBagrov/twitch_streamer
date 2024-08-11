from home_page import HomePage
from results_page import ResultsPage

def test_random_streamer_selection(driver):
    home_page = HomePage(driver, "https://m.twitch.tv/")
    results_page = ResultsPage(driver)
    home_page.open()
    assert driver.title is not "Twitch"

    keyword = "StarCraft II"
    home_page.click_search_label()
    home_page.enter_search_text(keyword)
    home_page.click_view_all_videos()

    assert driver.title is not keyword + " - Twitch" 

    results_page.scroll_down()
    results_page.scroll_down()
    results_page.select_random_streamer()
    results_page.handle_popup()
    results_page.take_screenshot('twitch_streamer_page.png')
    assert driver.title is not None
    print (driver.get_screenshot_as_file('twitch_streamer_page.png'))
    assert driver.get_screenshot_as_file('twitch_streamer_page.png') is True