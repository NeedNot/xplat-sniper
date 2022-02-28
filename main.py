from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import json
import time
from openpyxl import Workbook

x = input("Platform 1 (pc, psn, xbox, switch): ")
service = EdgeService(executable_path="edgedriver_win64/msedgedriver.exe")

options = Options()
#options.add_argument("headless")
options.add_argument("--start-fullscreen");

driver = webdriver.Edge(options = options, service=service)
url1 = ("https://rl.insider.gg/en/"+x)
driver.get(url1)
html = driver.page_source
soup1 = BeautifulSoup(html, "html.parser")
time.sleep(1)
driver.quit()
#url2 = ("https://rl.insider.gg/en/"+input("Platform 2 (pc, psn, xbox, switch): "))

#platform_2 =

#soup2 = BeautifulSoup(platform_1.content, "html.parser")

class Item:
    def __init__(self):
        self.name = None
        self.default = 0
        self.black = 0
        self.white = 0
        self.grey = 0
        self.crimson = 0
        self.pink = 0
        self.cobalt = 0
        self.skyblue = 0
        self.burnt = 0
        self.saffron = 0
        self.lime = 0
        self.green = 0
        self.orange = 0
        self.purple = 0

#workbook = Workbook()
#sheet = workbook.active

def get_paint(i, price, item):
    x = i % 15
    match x:
        case 1:
            item.default = price
        case 2:
            item.black = price
        case 3:
            item.white = price
        case 4:
            item.grey = price
        case 5:
            item.crimson = price
        case 6:
            item.pink = price
        case 7:
            item.cobalt = price
        case 8:
            item.skyblue = price
        case 9:
            item.burnt = price
        case 10:
            item.saffron = price
        case 11:
            item.lime = price
        case 12:
            item.green = price
        case 13:
            item.orange = price
        case 14:
            item.purple = price

def write(item, i):
    print(item.name)
    print(item.default)
    print(item.black)
    print(item.white)
    print(item.grey)
    print(item.crimson)
    print(item.pink)
    print(item.cobalt)
    print(item.skyblue)
    print(item.burnt)
    print(item.saffron)
    print(item.lime)
    print(item.green)
    print(item.orange)
    print(item.purple)
item_list = []

def painted_bms(soup1):
    results = soup1.find(id="paintedBMDecalsPrices")
    price_elements = results.find("tbody").find_all("tr")
    for items in price_elements:
        i = 14
        item = Item()
        #print(item)
        for paint in items.find_all("td"):
            i += 1
            price = paint.text
            if price != '-' and i % 15 == 0:
                name = price[:int(len(price)/2)]
                item.name = name
            else:
                get_paint(i, price, item)
        #write(item, i-13)
        item_list.append(item)
print(item_list)
#workbook.save(filename="prices.xlsx")
painted_bms(soup1)