# import requests
# from bs4 import BeautifulSoup

# page = requests.get('https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/')
# soup = BeautifulSoup(page.content,'html.parser')

# #extract title of the page
# page_title = soup.title.text
# #extract body of the page 
# page_body = soup.body.text

# print(page_body , page_title)

import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_title, page_head)