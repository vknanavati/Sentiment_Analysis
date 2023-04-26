import time
import re
from urllib.request import urlopen

# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = Options()

# Test case: London, England EUROPE


url = "https://www.hostelworld.com/st/hostels/europe/england/london/"
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")
soup.prettify()


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)
options.add_experimental_option("useAutomationExtension", False)
service = Service("C:/Users/viminnanavati/chromedriver.exe")

browser = webdriver.Chrome(
    options=options,
    service=service,
)
browser.get(url)
time.sleep(4)

url_list = []

results = browser.find_element(
    By.XPATH,
    "//main/div[4]/section",
)

raw_string = results.get_attribute("innerText").replace("\n", "")
digit_string = re.sub("[^0-9]", "", raw_string)
digit_list = [int(page) for page in digit_string]
print(digit_list)

# print(list())
# print(results.get_attribute("innerText").replace('\n', ''))


time.sleep(10)

browser.quit()


# https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/
# https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/p/2/

# page_list = []
# for character in results:
#     if (character.get_attribute("innerText") != "null"):
#         page_list.append(character.get_attribute("innerText"))
# print(page_list)

# for number in results:
#     page = number.text.strip()
#     page_list.append(page)

# print(*page_list)
# re.sub("[^0-9]", ", ", )

# page_list = *page_list, sep="\n"
# print(page_list)
# print(*page_list, sep="\n")
