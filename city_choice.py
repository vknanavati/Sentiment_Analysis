import time
import json
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

with open("continent_dict.json", encoding="UTF-8") as country_dict:
    country_dict = country_dict.read()

country_dict = json.loads(country_dict)


# user enters country name
def user_country():
    country_choice = input("\nEnter country: ")
    return country_choice


country = user_country()


# country variable used to get continent name from dictionary to autofill into country url
def get_continent():
    # item = value of k:v
    for item in country_dict.values():
        print(f"\nCountries of continent: {item}\n")
        # element represents the country in the list of countries from dictionary that country variable will be compared against
        for element in item:
            # country is the user's choice
            if country == element:
                continent_dict = [k for k, v in country_dict.items() if v == item][0]
                print(f"\nContinent of country: {continent_dict}\n")
                return continent_dict


continent = get_continent()

city_list = []


# accesses main hostel page for user country using continent, country variables
def get_cities():
    # generates list of cities with hostels in that country
    url = f"https://www.hostelworld.com/st/hostels/{continent}/{country}/"
    print(f"\nURL to be opened: {url}\n")
    html = urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()

    # testing to see if data can be accessed in url above
    # for info in soup.find("div", class_="properties-count"):
    # print(info.text)

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
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

    select_housing = Select(
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//select[@title='Find']",
                )
            )
        )
    )
    select_housing.select_by_index(0)

    select_location = Select(
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//select[@title='in']",
                )
            )
        )
    )

    select_location.select_by_index(1)
    time.sleep(20)

    results = browser.find_elements(
        By.XPATH,
        "//div[@class='selection-container'][3]/label/select/option[position()>1]",
    )

    # city_list = []
    for result in results:
        city = result.text
        city_list.append(city)
    # print(city_list)
    # print(*city_list, sep="\n")

    time.sleep(10)

    browser.quit()


get_cities()


def dict_cities():
    digit = [num + 1 for num in range(len(city_list))]

    # make dictionary
    joint_list = zip(digit, city_list)
    city_dict = dict(joint_list)
    print(city_dict)

    return city_dict


dictionary_cities = dict_cities()


def list_cities():
    # create list of numbers for each city in city_list
    number_list = [num + 1 for num in range(len(city_list))]

    # add periods to each number
    number_list = [f"{num}. " for num in number_list]

    number_city_list = [num + city for num, city in zip(number_list, city_list)]
    print(number_city_list)
    return number_city_list


city_choices = list_cities()

# print(*city_choices, sep="\n")


def choose_city():
    print("\nCHOOSE A CITY:\n")
    # unpacks city_choice list - user sees each item in a new line
    print(*city_choices, sep="\n")
    city_choice = input("\nEnter city by digit: ")

    if city_choice in dictionary_cities:
        pass

    # user enters number
    # open web page based on city choice


choose_city()
# next def should scan country page for pagination of hostel lists


#     url = f"https://www.hostelworld.com/st/hostels/{continent}/{city_choice}/"
#     html = urlopen(url)

#     soup = BeautifulSoup(html, "html.parser")
#     soup.prettify()

#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option("useAutomationExtension", False)
#     service = Service("C:/Users/viminnanavati/chromedriver.exe")

#     browser = webdriver.Chrome(
#         options=options,
#         service=service,
#     )
#     browser.get(url)
#     time.sleep(4)

#     # https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/
#     # https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/p/2/
