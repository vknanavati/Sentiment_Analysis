import time
from urllib.request import urlopen
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = Options()


def userCountry():
    user_input = input("Enter country: ")
    return user_input


country = userCountry()


def getCities():
    # accesses main hostel page for user country
    url = f"https://www.hostelworld.com/st/hostels/north-america/{country}/"
    html = urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()

    # testing to see if data can be accessed in url above
    # for info in soup.find("div", class_="properties-count"):
    # print(info.text)

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

    selectHousing = Select(
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//select[@title='Find']",
                )
            )
        )
    )
    selectHousing.select_by_index(0)

    selectLocation = Select(
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//select[@title='in']",
                )
            )
        )
    )

    selectLocation.select_by_index(1)
    time.sleep(20)

    city_list = []

    results = browser.find_elements(
        By.XPATH,
        "//div[@class='find-in-country']/div[@class='selection-container'][3]/label/select/option[position()>1]",
    )
    for result in results:
        city = result.text
        city_list.append(city)
    # print(city_list)
    print(*city_list, sep="\n")
    # for result in results:
    #     print(result.text)

    time.sleep(10)

    browser.quit()

    print("\ncountry hostel worked\n")


getCities()
