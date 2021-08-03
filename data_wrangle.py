import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests


data_url ='https://en.wikipedia.org/wiki/Road_safety_in_Europe'

page = requests.get(data_url)
table_class="wikitable sortable jquery-tablesorter"

if page.status_code ==200:

  soup = BeautifulSoup(page.text, 'html.parser')
  table=soup.find('table',{'class':"wikitable sortable"})
  df=pd.read_html(str(table))
  df=pd.DataFrame(df[0])
  A_sorted = df.sort_values("Total Road Deaths in 2018[30]")
  df.to_csv('data.csv')
