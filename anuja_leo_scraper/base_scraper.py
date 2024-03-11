import os
import time
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from utils import get_current_date, save_html
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# Load environmental variables
load_dotenv()

STORAGE_DIR_PATH = Path(os.getenv("STORAGE_PATH", "/tmp/anuja"))
CURRENT_DATE = get_current_date()
PAGE_WAIT_TIME = os.getenv("PAGE_WAIT_TIME", 20)

# TODO: Get alternate folder path for storage

HTML_DIR = STORAGE_DIR_PATH / CURRENT_DATE
BASE_HTML_FILEPATH = HTML_DIR / "base_page.html"
BASE_URL = os.getenv("BASE_URL")

# Create directory if not exists
Path(HTML_DIR).mkdir(parents=True, exist_ok=True)

print(f"Storage directoy {BASE_HTML_FILEPATH=}")

try:
    options = Options()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    time.sleep(int(PAGE_WAIT_TIME))
    save_html(driver.page_source, BASE_HTML_FILEPATH)

    print(f"Stored Base HTML in {STORAGE_DIR_PATH}")
    driver.quit()
except TimeoutException as timeout_resp:
    print(f"Error: {timeout_resp}")
