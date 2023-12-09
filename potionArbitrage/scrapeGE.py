from potionArbitrage.itemList import ITEM_LIST
import requests
import datetime
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pyppdf.patch_pyppeteer

# https://osrsgetracker.com/items/stamina-potion-1/
# https://www.ge-tracker.com/item/stamina-potion-1
# Send a GET request to the URL
url='https://www.ge-tracker.com/item/stamina-potion-1'
session = HTMLSession()

resp = session.get(url)
resp.html.render()
html = resp.html.html

soup = BeautifulSoup(html, 'html.parser')
table_responsive = soup.find("div", class_='table-responsive')
table_responsive.find('span', class_='has-tooltip v-tooltip-open').text.strip()
table_responsive.find('span', class_='has-tooltip').text.strip()
table_responsive.find('table').text.strip()
# price = soup.find(id='itemCurrentAskValue').text.strip()
# Print the results
# print(f"Ask: {price}")