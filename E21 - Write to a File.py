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
file_content = "\n".join([x.text for x in h3])

# open the specified file as a variable (or create if does not exist) and write to it; autocloses once done
# "w" is "write only" and overwrites the existing file; "r" is "ready only"; both would be "r+"
# .write autosaves after each statement
with open('NYTimes_headlines.txt', "w") as open_file:
    open_file.write(file_content)