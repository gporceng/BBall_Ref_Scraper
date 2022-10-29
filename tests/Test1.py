import requests
from bs4 import BeautifulSoup


URL = "https://www.basketball-reference.com/players/a/abdulka01.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="totals")
#print(results.prettify())

job_elements = results.find_all("td", class_="right")

#pts = job_elements.find(data_stat="pts")

#print(job_elements.find_all("p",class_="right"))   

#print(job_elements.find_all("data_set_","td"))
#for job_element in job_elements:
    #print(job_element, end="\n"*2)

#print(job_element.find("td","ft"))
table_body = results.find('tbody')

data = [["Season","Age","Tm","Lg","Pos","G","GS","MP","FG","FGA","FG%","3P","3PA","3P%","2P","2PA","2P%","eFG%","FT","FTA","FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS","Trp Dbl"]]
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

#print(len(data))

#print(data[19])

#for row in data:
    #print(row)

print(len(data))
print(len(data[0]))
print(len(data[20]))
print(data[20][29])
#print(pts.text)
f = open("myfile.txt", "w")
f.write("test")
#print(page.text)