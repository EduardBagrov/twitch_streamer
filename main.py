from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from home_page import HomePage
from results_page import ResultsPage

mobile_emulation = {
    "deviceMetrics": {"width": 1024, "height": 768, "pixelRatio": 1.0},
    "userAgent": (
        "Mozilla/5.0 (X11; CrOS x86_64 14588.0.0) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/97.0.4692.77 Safari/537.36"
    ),
}

base_url = "https://m.twitch.tv/"

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    home_page = HomePage(driver, base_url)
    results_page = ResultsPage(driver)

    home_page.open()
    home_page.click_search_label()
    home_page.enter_search_text("StarCraft II")
    home_page.click_view_all_videos()

    results_page.scroll_down()
    results_page.scroll_down()
    results_page.select_random_streamer()
    results_page.handle_popup()
    results_page.take_screenshot('twitch_streamer_page.png')

finally:
    driver.quit()
