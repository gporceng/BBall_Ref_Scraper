import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

r = requests.get("https://www.basketball-reference.com/players/a/abdulka01.html")
soup = bs(r.content, "html.parser")
#print(soup.prettify)

table = soup.select('table#per_game')[0]
columns = table.find('thead').find_all('th') 

#print(columns)

table_df = pd.read_html(str(table))[0] 

print(table_df) 