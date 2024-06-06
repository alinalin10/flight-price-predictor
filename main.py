import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

print("working")

#base_url = "https://www.coingecko.com/"
base_url = "https://www.tradingview.com/markets/cryptocurrencies/prices-all/"

tables = []
test = []

for i in range(1, 4):
    print(f"processing page number {i}")
    params = {
        'page': i
    }
    response = requests.get(base_url,headers={"User-Agent":"Mozilla/5.0"}, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    tables.append(pd.read_html(str(soup))[0])
    break

table_1 = pd.concat(tables)
table_1 = table_1.loc[:, table_1.columns[1:-1]]
table_1.to_csv("Crypto Data.csv", index=False)





