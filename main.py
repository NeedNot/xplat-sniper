from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import json
import time
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border

x = input("Platform 1 (pc, psn, xbox, switch): ")
service = EdgeService(executable_path="edgedriver_win64/msedgedriver.exe")

options = Options()
#options.add_argument("headless")
options.add_argument("--start-fullscreen");

driver = webdriver.Edge(options = options, service=service)
url1 = ("https://rl.insider.gg/en/"+x)
driver.get(url1)
time.sleep(10)
html = driver.page_source
soup1 = BeautifulSoup(html, "html.parser")
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
workbook = Workbook()
sheet = workbook.active
bold = Font(bold=True)

sheet["A1"] = "Item name"
sheet["A1"].font = bold
sheet["B1"] = "Default"
sheet["B1"].font = bold
sheet["B1"].fill = PatternFill(start_color='cac3b8', end_color='cac3b8', fill_type='solid')
sheet["C1"] = "Black"
sheet["C1"].font = bold
sheet["C1"].fill = PatternFill(start_color='000000', end_color='000000', fill_type='solid')
sheet["D1"] = "White"
sheet["D1"].font = bold
sheet["D1"].fill = PatternFill(start_color='ffffff', end_color='ffffff', fill_type='solid')
sheet["E1"] = "Grey"
sheet["E1"].font = bold
sheet["E1"].fill = PatternFill(start_color='999999', end_color='999999', fill_type='solid')
sheet["F1"] = "Crimson"
sheet["F1"].font = bold
sheet["F1"].fill = PatternFill(start_color='ff6363', end_color='ff6363', fill_type='solid')
sheet["G1"] = "Pink"
sheet["G1"].font = bold
sheet["G1"].fill = PatternFill(start_color='f89eff', end_color='f89eff', fill_type='solid')
sheet["H1"] = "Cobalt"
sheet["H1"].font = bold
sheet["H1"].fill = PatternFill(start_color='506ec9', end_color='506ec9', fill_type='solid')
sheet["I1"] = "Skyblue"
sheet["I1"].font = bold
sheet["I1"].fill = PatternFill(start_color='63ffff', end_color='63ffff', fill_type='solid')
sheet["J1"] = "Burnt"
sheet["J1"].font = bold
sheet["J1"].fill = PatternFill(start_color='b46f45', end_color='b46f45', fill_type='solid')
sheet["K1"] = "Saffron"
sheet["K1"].font = bold
sheet["K1"].fill = PatternFill(start_color='ffff63', end_color='ffff63', fill_type='solid')
sheet["L1"] = "Lime"
sheet["L1"].font = bold
sheet["L1"].fill = PatternFill(start_color='63ff63', end_color='63ff63', fill_type='solid')
sheet["M1"] = "Green"
sheet["M1"].font = bold
sheet["M1"].fill = PatternFill(start_color='457337', end_color='457337', fill_type='solid')
sheet["N1"] = "Orange"
sheet["N1"].font = bold
sheet["N1"].fill = PatternFill(start_color='ffaa63', end_color='ffaa63', fill_type='solid')
sheet["O1"] = "Purple"
sheet["O1"].font = bold
sheet["O1"].fill = PatternFill(start_color='a862fc', end_color='a862fc', fill_type='solid')



def write(item, i):
    sheet[f"A{i}"] = item.name
    sheet[f"B{i}"] = item.default
    sheet[f"C{i}"] = item.black
    sheet[f"D{i}"] = item.white
    sheet[f"E{i}"] = item.grey
    sheet[f"F{i}"] = item.crimson
    sheet[f"G{i}"] = item.pink
    sheet[f"H{i}"] = item.cobalt
    sheet[f"I{i}"] = item.skyblue
    sheet[f"J{i}"] = item.burnt
    sheet[f"K{i}"] = item.saffron
    sheet[f"L{i}"] = item.lime
    sheet[f"M{i}"] = item.green
    sheet[f"N{i}"] = item.orange
    sheet[f"O{i}"] = item.purple
item_list = []

def real_price(price):
    #print(price)
    price = price.split()
    if 'k' in price:
        multiplier = 1000
    elif 'm' in price:
        multiplier = 1000000
    else:
        multiplier = 1
    try:
        a = float(price[0])*multiplier
        print(a)
        return a
    except (ValueError, IndexError) as e:
        print(price)
        print(e)
        return 0
    

def painted_bms(soup1):
    results = soup1.find(id="paintedBMDecalsPrices")
    price_elements = results.find("tbody").find_all("tr")
    x = 0
    for items in price_elements:
        x += 1
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
                price = real_price(price)
                get_paint(i, int(price), item)
        item_list.append(item)
        write(item, x+1)
painted_bms(soup1)
workbook.save(filename="prices.xlsx")