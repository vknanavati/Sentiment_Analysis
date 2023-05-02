import time
import json
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()

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


url = "https://www.hostelworld.com/st/hostels"
html = urlopen(url)


soup = BeautifulSoup(html, "html.parser")
soup.prettify()

browser.get(url)
time.sleep(4)
##########################################
results = browser.find_elements(
    By.XPATH,
    "//div[@class='main']/div/main[@class='container']/div[@class='continents-list rwd-wrapper']/ul[@class='continents']/li[@class='continent']/button[@class='accordion-link']/h2/a",
)
time.sleep(6)

continent_list = []
for result in results:
    continent = result.get_attribute("text")
    continent_list.append(continent)
print(f"\nContinent list: {continent_list}\n")
# Continent list: ['Europe', 'Asia', 'North America', 'South America', 'Oceania', 'Africa']

time.sleep(3)
###################################

###################################
continent_class = soup.find_all("li", class_="continent")
time.sleep(2)
country_list = []
for continent in continent_class:
    continent = continent.find_all("li", class_="country")
    time.sleep(3)
    group_countries = [country.text.strip() for country in continent]
    country_list.append(group_countries)
print(f"\nCOUNTRY LIST: {country_list}\n")

time.sleep(10)
browser.quit()

lists_to_join = zip(continent_list, country_list)
joint_list = list(lists_to_join)


complete_dict = dict(joint_list)

print(f"\nCOMPLETE DICT:{complete_dict}\n")


with open("continent_dict.json", "w", encoding="UTF-8") as dict_cont:
    json.dump(complete_dict, dict_cont)
#########OUTPUT##########
# Continent list: ['Europe', 'Asia', 'North America', 'South America', 'Oceania', 'Africa']


# Country List: [['Albania', 'Andorra', 'Armenia', 'Austria', 'Belgium', 'Bosnia And Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales'], ['Azerbaijan', 'Bangladesh', 'Brunei', 'Cambodia', 'China', 'Hong Kong China', 'India', 'Indonesia', 'Iran', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'Pakistan', 'Palestine', 'Philippines', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Taiwan China', 'Tajikistan', 'Thailand', 'United Arab Emirates', 'Uzbekistan', 'Vietnam'], ['Antigua And Barbuda', 'Bahamas', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominican Republic', 'El Salvador', 'Guadeloupe', 'Guatemala', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Trinidad And Tobago', 'US Virgin Islands', 'USA'], ['Argentina', 'Aruba', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Martinique', 'Netherlands Antilles', 'Paraguay', 'Peru', 'Puerto Rico', 'Suriname', 'Uruguay', 'Venezuela'], ['Australia', 'East Timor', 'Fiji', 'French Polynesia', 'New Zealand'], ['Botswana', 'Cape Verde', 'Egypt', 'Ethiopia', 'Ghana', 'Kenya', 'Lesotho', 'Madagascar', 'Malawi', 'Morocco', 'Mozambique', 'Namibia', 'Nigeria', 'Reunion', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 'South Africa', 'Swaziland', 'Tanzania', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']]


# COMPLETE DICT:{'Europe': ['Albania', 'Andorra', 'Armenia', 'Austria', 'Belgium', 'Bosnia And Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales'], 'Asia': ['Azerbaijan', 'Bangladesh', 'Brunei', 'Cambodia', 'China', 'Hong Kong China', 'India', 'Indonesia', 'Iran', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'Pakistan', 'Palestine', 'Philippines', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Taiwan China', 'Tajikistan', 'Thailand', 'United Arab Emirates', 'Uzbekistan', 'Vietnam'], 'North America': ['Antigua And Barbuda', 'Bahamas', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominican Republic', 'El Salvador', 'Guadeloupe', 'Guatemala', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Trinidad And Tobago', 'US Virgin Islands', 'USA'], 'South America': ['Argentina', 'Aruba', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Martinique', 'Netherlands Antilles', 'Paraguay', 'Peru', 'Puerto Rico', 'Suriname', 'Uruguay', 'Venezuela'], 'Oceania': ['Australia', 'East Timor', 'Fiji', 'French Polynesia', 'New Zealand'], 'Africa': ['Botswana', 'Cape Verde', 'Egypt', 'Ethiopia', 'Ghana', 'Kenya', 'Lesotho', 'Madagascar', 'Malawi', 'Morocco', 'Mozambique', 'Namibia', 'Nigeria', 'Reunion', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 'South Africa', 'Swaziland', 'Tanzania', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']}
