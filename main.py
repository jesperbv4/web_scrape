import requests
from bs4 import BeautifulSoup

def response(url):
    url = url
    s = requests.Session()
    r = s.get(url)
    return r

def scraper(url):
    soup = BeautifulSoup(response(url).text, 'html.parser')
    return soup

def data_extract(url):
    results = scraper(url).find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    cities = [results[i].contents[0] for i in range(len(results)-1)]  
    links = [results[i].get('href') for i in range(len(results)-1)]
    city_links = {cities[i]: links[i] for i in range(len(cities))}
    return city_links

def temp_extract(url):
    results = scraper(url).find_all('div', attrs={'class': 'item weather'})
    temp_high = [int(results[i].find('span').find_all('span')[0].contents[0][0:-1]) for i in range(len(results)-1)]
    temp_low =  [int(results[i].find('span').find_all('span')[2].contents[0][0:-1]) for i in range(len(results)-1)]
    temp = [(temp_high[i], temp_low[i]) for i in range(len(temp_high))]
    return temp

if __name__ == "__main__":
    standard_input= ''  #Behövs för ett tillägg jag använder
    url = 'https://www.klart.se/'
    print(data_extract(url))
