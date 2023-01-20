import requests
from bs4 import BeautifulSoup
url = "https://insights.blackcoffer.com/the-future-of-investing/"

#step1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
print (htmlContent)


#step2: parse the HTML
#step#: HTML Tree traversal