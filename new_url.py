import requests
from bs4 import BeautifulSoup

def response(url):
        url = url
        s = requests.Session()
        r = s.get(url)
        return r

def data_extract(results):
    print(len(results))
    cities = [results[i].contents[0] for i in range(len(results)-1)]  
    links = [results[i].get('href') for i in range(len(results)-1)]
    res = {cities[i]: links[i] for i in range(len(cities))}
    return res

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


url1 = 'https://www.klart.se'

def new_page(url):
    data = response(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    results_ = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    res = (data_extract(results_))
    new_url = url + choose_dict(res)
    return new_url


# data = response(new_url)
# soup = BeautifulSoup(data.text, 'html.parser')
# results_ort = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
# res = (data_extract(results_ort))
# new_url2 = new_url + choose_dict(res)
# print(new_url2)

print(new_page(new_page(url1)))