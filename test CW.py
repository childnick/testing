import os
import csv
import json
import time
import base64
import datetime
import requests

import mysql.connector

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from multiprocessing.pool import ThreadPool, Pool

import threading

print("Start")

chrome_options = Options()
prefs = {'profile.managed_default_content_settings.images': 2} #hide images - 2 is the code for that option
chrome_options.add_experimental_option('prefs', prefs)
#chrome_options.add_extension('C:/Python/Tools/Drivers/AdBlock_v3.42.0.crx') #chrome doesn't support headless extensions currently :(
chrome_options.add_argument("--headless")

chrome_options.binary_location = "C:/Users/Administrator/AppData/Local/Google/Chrome SxS/Application/chrome.exe"
driver = webdriver.Chrome("C:/Users/Administrator/AppData/Local/Programs/Python/Python37-32/Tools/Drivers/chromedriver.exe",   options=chrome_options)

driver.get("http://www.cineworld.co.uk")
# cookies = {c["name"]: c["value"] for c in driver.get_cookies()}
print(driver.get_cookies())

# print(cookies)
driver.quit()




# session = requests.Session()
# session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

# url = 'https://www.cineworld.co.uk/booking?presentationCode=117178&cinemaId=8014'
# print("Scraping: ",url)
# first = session.get(url)
# session_id = (first.headers["X-UserSessionID"])
# cookie = first.headers["Set-Cookie"]
# print(first.headers)
# print(first.cookies.get_dict())
# print()
# print()

# tempurl = 'https://booking.cineworld.co.uk/booking/8014/117178/' + str(session_id) +'/tickets'
# print("Scraping: ",tempurl)
# tempdata = session.get(tempurl)
# # cookie = tempdata.headers["Set-Cookie"]
# print(tempdata.headers)
# print(tempdata.cookies)
# print()


# # newurl = 'https://booking.cineworld.co.uk/booking/8014/117178/' + str(session_id) +'/seats-plan'
# # print("Scraping: ",newurl)
# # info = session.post(newurl,headers={'Referer':tempurl,'Host':'booking.cineworld.co.uk','Origin':'https://booking.cineworld.co.uk','Cookie':cookie})
# # print(info.text)

# # https://www.cineworld.co.uk/booking?presentationCode=117178&cinemaId=8014

