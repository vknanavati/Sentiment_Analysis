from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

browser = webdriver.Chrome()  # start a web browser
browser.get("https://www.airbnb.com/experiences/272085")  # navigate to URL
# wait for page to load
# by waiting for <h1> element to appear on the page
title = (
    WebDriverWait(driver=browser, timeout=10)
    .until(visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    .text
)
# retrieve fully rendered HTML content
content = browser.page_source
browser.close()

# we then could parse it with beautifulsoup
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, "html.parser")
print(soup.find("h1").text)
