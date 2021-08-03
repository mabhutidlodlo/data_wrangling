import requests
from bs4 import BeautifulSoup
import requests
import csv


data_url ='https://en.wikipedia.org/wiki/Road_safety_in_Europe'

page = requests.get(data_url)

if page.status_code ==200:

  soup = BeautifulSoup(page.text, 'html.parser')
  table=soup.find('table',{'class':"wikitable sortable"})
  data = []
  for tr in table.find_all('tr'):
    td = tr.find_all('td')
    row = [i.get_text(strip=True) for i in td]
    if len(row) != 0:
      new_row = [row[0],2018,row[1],row[2],row[3],row[4],row[5], row[7],row[8]]
      data.append(new_row)

  sorted = sorted(data, key=lambda row: (int(row[8])))

    
  with open('../data/data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    headers = ["Country","Year","Area","Population","GDP per capita","Population density","Vehicle ownership","Total Road Deaths","Road deaths per Million Inhabitants"] 
    writer.writerow(headers)
    writer.writerows(sorted)