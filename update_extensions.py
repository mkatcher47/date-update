#!/usr/bin/env python3

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, date, timedelta
import calendar

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## Load List of Claimants for Follow Up Date Update

with open("claimantlist.csv", newline='', encoding='utf-8-sig') as csvfile:
    extension_date_list = csv.reader(csvfile, delimiter=',')
    claimants_list = []
    for row in extension_date_list:
        claimants_list.append(row)

## Set New Follow Up Date
## The follow up date is set to thirty days from today's date, unless it is over a weekend, in which case it is set to Monday.

new_date = date.today() + timedelta(days = 30)

if new_date.weekday() == 5:
    new_date = new_date + timedelta(days = 2)
elif new_date.weekday() == 6:
    new_date = new_date + timedelta(days = 1)
else:
    pass

## Update Follow Up Date on Page
## The page is loaded for each claimant using a csv file containing the page IDs. 

for row in claimants_list:
    browser.get("internalsite.com/Edit.aspx?Id="+str(row[0]))

    browser.maximize_window()
    time.sleep(1)

    extension_date = browser.find_element(By.ID, "date_input_field")

    extension_date.clear()
    extension_date.send_keys(str(newdate))

    ok_button = browser.find_element(By.ID, "ok_button")
    ok_button.click()
