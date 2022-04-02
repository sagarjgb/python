import requests
from bs4 import BeautifulSoup
url='https://www.google.com/finance/quote/NIFTY_50:INDEXNSE?sa=X&ved=2ahUKEwjz7rHajtD2AhWBzTgGHRLmBVIQ3ecFegQIDxAY'
response=requests.get(url)
soup=BeautifulSoup(response.text)
result=soup.select('.YMlKec.fxKbKc')
result1=soup.select('.ygUjEc')
rs2=soup.select('.zWwE1')
print(result[0].getText())
print(rs2[0].getText())
print(result1[0].getText())
