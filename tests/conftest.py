import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    mobile_emulation = {
    "deviceMetrics": {"width": 1024, "height": 768, "pixelRatio": 1.0},
    "userAgent": (
        "Mozilla/5.0 (X11; CrOS x86_64 14588.0.0) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/97.0.4692.77 Safari/537.36"
        )
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()
