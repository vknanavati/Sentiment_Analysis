import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome()

driver.get(
    "https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS"
)
more_buttons = driver.find_elements(By.CLASS_NAME, "moreLink")
for x in range(len(more_buttons)):
    if more_buttons[x].is_displayed():
        driver.execute_script("arguments[0].click();", more_buttons[x])
        time.sleep(1)
page_source = driver.page_source

print(page_source)

from bs4 import BeautifulSoup

# soup = BeautifulSoup(page_source, "html.parser")
# reviews = []
# reviews_selector = soup.find_all("div", class_="reviewSelector")
# for review_selector in reviews_selector:
#     review_div = review_selector.find("div", class_="dyn_full_review")
#     if review_div is None:
#         review_div = review_selector.find("div", class_="basic_review")
#     review = review_div.find("div", class_="entry").find("p").get_text()
#     review = review.strip()
#     reviews.append(review)

# print(reviews)
