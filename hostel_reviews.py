# import time
# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# import selenium.common.exceptions as exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)
options.add_experimental_option("useAutomationExtension", False)

browser = webdriver.Chrome(
    chrome_options=options, executable_path=r"C:/Users/viminnanavati/chromedriver.exe"
)
browser.get(
    "https://www.hostelworld.com/st/hostels/p/307620/casa-kanabri-hostal-boutique/?display=reviews"
)

title = (
    WebDriverWait(driver=browser, timeout=10)
    .until(visibility_of_element_located((By.CLASS_NAME, "review-notes")))
    .text
)
content = browser.page_source
browser.close()

# page = requests.get(URL, timeout=10)


soup = BeautifulSoup(content, "html.parser")
for submission in soup.find_all("div", class_="review-notes"):
    print(submission.text)
# soup.prettify()

# for submission in soup.find_all("div", class_="review-notes"):
#     print(submission.text)

# for topic in soup.find_all("h3"):
#     print(topic.text)
#     info = topic.find_next_sibling("p")
#     print(info.text.strip())
#     print()

# user_input = input("Please enter country name")


# headings = []
# data = []
# for topic in soup.find_all("h3"):
#     headings.append(topic.text)

#     info = topic.find_next_sibling("p")
#     data.append(info.text)
# # print(headings)
# # print()
# # print(data)

# lists_to_join = zip(headings, data)
# joint_list = list(lists_to_join)


# country_dict = dict(joint_list)


# keys = {
#     "US State Dept Travel Advisory",
#     "Climate",
#     "Currency",
#     "Major Languages",
#     "Road Driving Side",
#     "Tourist Destinations",
#     "Cultural Practices",
#     "Tipping Guidlines",
#     "Traditional Cuisine",
# }

# new_dict = {key: value for key, value in country_dict.items() if key in keys}
# # print(new_dict)

# new_dict = {
#     "US State Dept Travel Advisory": "The US Department of State currently recommends US citizens exercise normal precautions in Switzerland. Consult its website via the link below for updates to travel advisories and statements on safety, security, local laws, and special circumstances in this country.https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html",
#     "Climate": "Temperate, but varies with altitude; cold, cloudy, rainy/snowy winters; cool to warm, cloudy, humid summers with occasional showers",
#     "Major Languages": "German (or Swiss German), French, Italian, English, Portuguese, Albanian, Serbo-Croatian, Spanish",
#     "Road Driving Side": "Right",
#     "Tourist Destinations": "Matterhorn; Jungfraujoch; Interlaken; Lucerne; Lake Geneva; Chateau de Chillon; Zurich; Lake Lugano; Bern",
#     "Cultural Practices": "Speaking too loudly in public, especially on cell phones, is frowned upon.",
#     "Traditional Cuisine": "Rösti — grated potato patties sometimes including herbs and spices, onions, ham, or cheese and pan-fried in butter or oil; the dish is cut into wedges for serving",
# }


# with open("country_dict_df.json", encoding="UTF-8") as country_dict_list:
#     country_dict_list = country_dict_list.read()
# # print(f"data:{country_dict_list}")
# country_dict_list = json.loads(country_dict_list)
# df = pd.DataFrame(country_dict_list)
# print(df)
