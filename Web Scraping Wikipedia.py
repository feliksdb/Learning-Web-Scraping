# -*- coding: utf-8 -*-
"""Scraping Wikipedia.ipynb
"""

#Import modules for Web Scraping
from bs4 import BeautifulSoup
import requests

#Below are the 100 largest companies by revenue in 2023 (mostly for fiscal year 2022), according to the Fortune 500 list. Scraped January 28 2024

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find_all('table')[1]

soup.find('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1]

print (table)

world_titles = table.find_all('th')

world_titles

world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

#Import modules for Data Processing
import pandas as pd

#Create Data Frame
df = pd.DataFrame(columns = world_table_titles)
df

#Create Data Frame II
column_data = table.find_all('tr')

#Create Data Frame III
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

#Check Data Frame
df

#Export Data to Google Colab Directory
df.to_csv('/content/drive/MyDrive/Colab Notebooks/Companies.csv', index = False)
