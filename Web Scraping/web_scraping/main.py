import requests
import bs4
import lxml.html

res = requests.get("https://example.com/")
#print(type(res))

#print(res.text)
soup = bs4.BeautifulSoup(res.text,"lxml")
elem = soup.select('title') # pass name of element in commas to pick up raw elements

print(elem[0].getText())





