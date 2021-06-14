import requests
from bs4 import BeautifulSoup

# request the vanity fair article
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

# select the string containing HTML for interpretation
soup = BeautifulSoup(r_html, "html.parser")

# extract the headline and description text from specific elements using element selectors and find
# all_text = soup.get_text()
title = soup.h1.string
abstract = soup.find("div", class_="content-header__dek").string

# extract the paragraph text
text = soup.find_all("p")
text = [x.string for x in text if x.string != None]

# combine into one string
article = title + "\n" + abstract + "\n" + " ".join(text)