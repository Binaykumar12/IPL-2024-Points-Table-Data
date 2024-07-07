import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/points-table/men/2024"
r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.text,"lxml")
table= soup.find("table",class_="ih-td-tab")
# print(table)
title=table.find_all("th")
# print(title)

header=[]
for i in title:
    name=i.text
    header.append(name)

df= pd.DataFrame(columns=header)
print(df)

rows= table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    print("data")