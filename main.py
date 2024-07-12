import requests
from bs4 import BeautifulSoup
import pandas as pd
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept-Language': 'en-US, en;q=0.5'
}
url="https://www.amazon.com/s?k=speaker"
r=requests.get(url, headers=HEADERS)
# print(r)

soup=BeautifulSoup(r.content, "html.parser")
print(soup)
links= soup.find_all("span",attrs={'class': 'a-size-medium a-color-base a-text-normal'})
links_list = [link.text for link in links if 'charge' not in link.text]
# # print(table)
# title=table.find_all("th")
# # print(title)

# header=[]
for i in links_list:
    name=i
    print(name)
#     header.append(name)

# df= pd.DataFrame(columns=header)
# print(df)

# rows= table.find_all("tr")
# for i in rows[1:]:
#     data=i.find_all("td")
#     print("data")