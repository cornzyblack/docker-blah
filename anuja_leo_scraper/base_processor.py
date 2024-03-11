from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from utils import get_current_date
from pathlib import Path
import re

load_dotenv()

#  Check if HTML file exists

STORAGE_DIR_PATH = Path(os.getenv("STORAGE_PATH", "/tmp/anuja"))
CURRENT_DATE = get_current_date()
PAGE_WAIT_TIME = os.getenv("PAGE_WAIT_TIME", 20)

# TODO: Get alternate folder path for storage

HTML_DIR = STORAGE_DIR_PATH / CURRENT_DATE
BASE_HTML_FILEPATH = HTML_DIR / "base_page.html"

soup = None

if BASE_HTML_FILEPATH.exists():
    with open(BASE_HTML_FILEPATH, "r") as f:
        html_str = f.read()
        soup = BeautifulSoup(html_str, "html.parser")

phone_details = []

phone_catalog_html_tree = soup.select("main > div > div:first-of-type")
if phone_catalog_html_tree:
    all_phones_div = phone_catalog_html_tree[0].find_all(
        "div", {"class": re.compile("ProductItemGrid_gridItemWrapper__.*")}
    )
    print(all_phones_div)
    # if all_phones_div:
    #     for phone_div in all_phones_div:
    #         {
    #             '': None
    #         }
    #         a_href_phone_det = phone_div.find_all(
    #             "a", {"class": re.compile("ProductItemGrid_image__.*")}
    #         )
    #         print(a_href_phone_det)
    #         if a_href_phone_det:
    #             print(a_href_phone_det[0].text)
