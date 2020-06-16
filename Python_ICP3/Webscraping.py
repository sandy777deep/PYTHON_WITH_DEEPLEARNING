
import requests
import re

from bs4 import BeautifulSoup

url = input("Please enter the Wiki URL: ")

html = requests.get(url)

bsObj = BeautifulSoup(html.content, "html.parser")

print("Title: " + bsObj.title.string)

links_list = bsObj.find_all('a', attrs={'href': re.compile("^http")})

print("Number of links: " + str(len(links_list)))

with open("links.txt", 'w') as f:
  temp = [f.write(str(link.get('href')) + '\n') for link in links_list]
