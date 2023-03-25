import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

n = []
l = []
cur_page = 0
cur_max = 7
while cur_page < cur_max:
     req = requests.get('https://realt.by/sale/flats/')
     ht = BeautifulSoup(req.content, 'html.parser')
#price = enumerate(ht.find_all('div', class_='col-auto text-truncate'))
     for counter, a in enumerate(ht.find_all('a', class_='teaser-title')):
          n.append(a.text.strip())
          print(a.text.strip())
          l.append((a['href']))
          print(a['href'])
     cur_page += 1

d = {'Name':n,
     'Age':l}
p = pd.DataFrame(d)
writer = pd.ExcelWriter('output.xlsx')
p.to_excel(writer, 'peuple')
writer.save()