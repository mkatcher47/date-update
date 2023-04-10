# Update the Date for Follow Up in Bulk

This program will update the follow up date for a bulk set of pages using a provided .csv file with page IDs.

## Create the list of Page IDs

With a provided list of names for follow up, us a VLOOKUP command in Excel to identify the associated page ID numbers. Save these numbers as a csv file as 'claimantlist.csv'.

## Run Update

### Install Selenium Package

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium.

```Bash
pip install -U selenium
```


```Python
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, date, timedelta
import calendar

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

## Load List of Claimants for Follow Up Date Update

```Python
with open("claimantlist.csv", newline='', encoding='utf-8-sig') as csvfile:
    extensionDateList = csv.reader(csvfile, delimiter=',')
    claimantslist = []
    for row in extensionDateList:
        claimantslist.append(row)
```

## Set New Follow Up Date
## The follow up date is set to thirty days from today's date, unless it is over a weekend, in which case it is set to Monday.

```Python
newdate = date.today() + timedelta(days = 30)

if newdate.weekday() == 5:
    newdate = newdate + timedelta(days = 2)
elif newdate.weekday() == 6:
    newdate = newdate + timedelta(days = 1)
else:
    pass
```

## Update Follow Up Date on Page
## The page is loaded for each claimant using a csv file containing the page IDs. 

```Python
for row in claimantslist:
    browser.get("internalsite.com/Edit.aspx?Id="+str(row[0]))

    browser.maximize_window()
    time.sleep(1)

    extension_date = browser.find_element(By.ID, "date_input_field")

    extension_date.clear()
    extension_date.send_keys(str(newdate))

    OK_button = browser.find_element(By.ID, "ok_button")
    OK_button.click()
```
