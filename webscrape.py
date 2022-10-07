import tempfile
import requests
from bs4 import BeautifulSoup


url = 'https://www.klart.se/se/uppsala-l%C3%A4n/v%C3%A4der-uppsala/'

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
temp = soup.find_all('div', attrs={'class': 'item weather'})


# for span in temp:
#     print(span)


for i in temp:
    span = i.find('span').find_all('span')
    print(f"Max {span[0].contents[0]}")
    print(f"Min {span[2].contents[0]}")
    print(span)
      