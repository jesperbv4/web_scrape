import tempfile
import requests
from bs4 import BeautifulSoup


url = 'https://www.klart.se/se/uppsala-l%C3%A4n/v%C3%A4der-uppsala/'

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
temp = soup.find_all('div', attrs={'class': 'item weather'})


# for span in temp:
#     print(span)


for obj in temp:
    item = obj.find('span').find('span')
    print(item.contents[0])
  