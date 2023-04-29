import time
from urllib.request import urlopen
import re
import requests

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
page = requests.get(url, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")

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


# def pagination_count():
if soup.find("section") is not None:
    pass
else:
    print("False")

time.sleep(8)
results = browser.find_element(
    By.XPATH,
    "//main/div[4]/section",
)

raw_string = results.get_attribute("innerText").replace("\n", "")
digit_string = re.sub("[^0-9]", "", raw_string)
digit_list = [int(page) for page in digit_string]

print(digit_list)

time.sleep(5)

browser.quit()

# url = "https://www.hostelworld.com/st/hostels/europe/england/london/"

list_len = len(digit_list)
# print(list_len)

url_list = [url for count in range(list_len)]
# print([url for count in range(list_len)])

i = 1
for link in range(1, len(url_list)):
    i = i + 1
    url_list[link] = url_list[link] + "/p/" + str(i) + "/"


print(url_list)

# ['https://www.hostelworld.com/st/hostels/europe/england/london/', 'https://www.hostelworld.com/st/hostels/europe/england/london/', 'https://www.hostelworld.com/st/hostels/europe/england/london/', 'https://www.hostelworld.com/st/hostels/europe/england/london/']

# for link in url_list:
# def create_list():


# url_list = []
# count = 0
# while count < len(digit_list):
#     url_list.append(url)


# return digit_list


# page_digits = pagination_count()
# page_digits = [1,2,3,4]


# checks to see if "section" tag exists. Cities without pagination will not have this tag and therefore will not need to go through pagination function
# if soup.find("section") is not None:
#     pagination_count()
# else:
#     print("False")
