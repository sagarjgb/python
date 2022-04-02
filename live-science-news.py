import requests
from bs4 import BeautifulSoup
url='https://news.google.com/search?q=science&hl=en-IN&gl=IN&ceid=IN%3Aen'
response=requests.get(url)
soup=BeautifulSoup(response.text)

result1=soup.select('.lBwEZb.BL5WZb.xP6mwf')

heading_tags = ["h1", "h2", "h3"]
subhead_tags=["h4","h5","h6"]
print("\t\t\t\t********************LIVE SCIENCE NEWS********************\n\n")
for tags in soup.find_all(heading_tags):
    print(tags.text.strip())
    print("\n")
    print("*****************************************************************************************************************************")
    print("\n")
