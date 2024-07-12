import requests
from bs4 import BeautifulSoup
import time
import random

url = "https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone%7CMobiles&requestId=6757079a-af9e-45b5-bc4f-526eceaeb7a1&as-searchtext=mobile%20"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

s = random.uniform(1, 3)
print(f"Sleeping for {s:.2f} seconds")
time.sleep(s)