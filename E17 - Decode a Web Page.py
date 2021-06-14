import requests
from bs4 import BeautifulSoup

# request the NYTimes website and extract the string containing the HTML
url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

# select the string containing HTML for interpretation
soup = BeautifulSoup(r_html, "html.parser")

# find an element by its CSS selector
h3 = soup.find_all("h3")
for x in h3:
    print(x.text)
