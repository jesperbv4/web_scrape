import requests
from bs4 import BeautifulSoup

#Skickar en get.requset och returnerar svaret
def response(url):
    url = url
    s = requests.Session()
    r = s.get(url)
    return r

#Skapar ett soup objekt från svaret av response
def scraper(url):
    soup = BeautifulSoup(response(url).text, 'html.parser')
    return soup

#Extraherar län och ort
def data_extract(url):
    results = scraper(url).find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    cities = [results[i].contents[0] for i in range(len(results)-1)]  
    links = [results[i].get('href') for i in range(len(results)-1)]
    city_links = {cities[i]: links[i] for i in range(len(cities))}
    return city_links

#Extraherar max och min temperatur från dagens datum och 14 dagar frammåt
def temp_extract(url):
    results = scraper(url).find_all('div', attrs={'class': 'item weather'})
    temp_high = [int(results[i].find('span').find_all('span')[0].contents[0][0:-1]) for i in range(len(results)-1)]
    temp_low =  [int(results[i].find('span').find_all('span')[2].contents[0][0:-1]) for i in range(len(results)-1)]
    temp = [(temp_high[i], temp_low[i]) for i in range(len(temp_high))]
    return temp

def indexify(dict):
    y = enumerate(dict, start=1)
    return y

def print_index(dict):
    for index, key in indexify(dict):
        print(f"{index}) {key}")

def choose_dict(dict):
    print_index(dict)
    while True:
        selected = select()
        for index, key in indexify(dict):
            if selected == str(index) or selected.capitalize() == key:
                return dict[key]

def select():
    return input("Option: ")

def new_page(url, snippet):
    new_url = url + snippet
    return new_url

def main():
    url = 'https://www.klart.se'
    

    
    



if __name__ == "__main__":
    main()
