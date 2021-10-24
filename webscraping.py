import json
import time
import sys
import pandas
from timeit import default_timer as timer
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

# ********************************
# Functions
# ********************************

def get_text_value_element(element):
    return BeautifulSoup(element.get_attribute('outerHTML'), 'html.parser').get_text()

def get_max_pagination():
    select = Select(driver.find_element_by_css_selector("select[title='Page Number Selection Drown Down List']"))
    last_option = select.options[len(select.options) - 1]
    return int(get_text_value_element(last_option))

def click_element(element):
    driver.execute_script("arguments[0].click();", element)

def get_elapsed_time():
    end_time = timer()
    return end_time - start_time

def get_elapsed_time_str(time):
    hours, remainder = divmod(time, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    
# ********************************
# Script
# ********************************
    
# Start Time
start_time = timer()

# NBA
url = "https://www.nba.com/players"
result = {}
players = []

options = Options()

console = Console()

MARKDOWN = f"""
# Webscraping - NBA 

A python script to gather NBA players' information.

URL: {url}

---
"""

console.print(Markdown(MARKDOWN))
    
print("\nConnecting to Selenium")
driver = webdriver.Remote("http://chrome:4444/wd/hub", options = options)

print("\nWebscrapping starting\n")
driver.get(url)
time.sleep(3) # in seconds

count = 1
max_pagination = get_max_pagination()
next_button = driver.find_element_by_css_selector("button[data-pos='next']")

with console.status("[bold green]Working on tasks") as status:
    while count <= max_pagination:
        console.log("Extracting page {start} of {end}".format(start = count, end = max_pagination))
        
        # Get table area element
        element = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[3]/section/div/div[2]")
        html_content = element.get_attribute('outerHTML')
        
        # Parse HTML - BeaultifulSoup.
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        # Convert to `dict`.
        data_frame = pandas.read_html(str(table))[0]

        # Transform the `data_frame` to have lower keys.
        for athlete in data_frame.to_dict('records'):
            dictWithLowerKey = { key.lower(): value for key, value in athlete.items() }
            players.append(dictWithLowerKey)
            
        click_element(next_button)
        
        time.sleep(0.5)
        
        count += 1

driver.quit()

# Add 'players' key to receive the list of players.
result['players'] = players

# Write .json file with the final result
with open('results.json', 'w', encoding='utf-8') as file:
    console.print('\nUploading [green].json[/] file\n')
    json.dump(result, file, ensure_ascii=False)
    
console.print(Markdown("---"))

elapsed = get_elapsed_time()

table = Table(title="Summary")

table.add_column("Total of players")
table.add_column("End time", justify="right")

table.add_row(str(len(result['players'])), get_elapsed_time_str(elapsed))

console.print(table)

print("\nEnd of the process\n")

sys.exit()