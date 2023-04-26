from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# import selenium.common.exceptions as exceptions
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select


# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


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
    for info in soup.find("div", class_="properties-count"):
        print(info.text)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    options.add_experimental_option("useAutomationExtension", False)

    browser = webdriver.Chrome(
        chrome_options=options,
        executable_path=r"C:/Users/viminnanavati/chromedriver.exe",
    )

    browser.get(url)
    time.sleep(4)

    # selectFind = Select(browser.find_element(By.TAG_NAME, "select"))
    # selectFind.select_by_value("hostel")
    # time.sleep(2)

    # selectHousing = Select(
    #     browser.find_element(
    #         By.XPATH,
    #         "//div[@class='find-in-country']/div[@class='selection-container'][1]",
    #     )
    # )

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
    print(city_list)
    # for result in results:
    #     print(result.text)

    time.sleep(10)

    # WebDriverWait(browser, 10)
    # browser.implicitly_wait(20)

    # cities = browser.find_element(
    #     By.XPATH,
    #     "//div[@class='find-in-country']/div[@class='selection-container'][3]",
    # )

    # for option in cities.options:
    #     print(option.text)

    browser.quit()

    print("\ncountry hostel worked\n")


getCities()
