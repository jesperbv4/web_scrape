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
        selected = int(select())
        for index, key in indexify(dict):
            if selected == index:
                return dict[key]

def select():
    return input("Option: ")


url = 'https://www.klart.se'
data = response(url)
soup = BeautifulSoup(data.text, 'html.parser')
results_län = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
res = (data_extract(results_län))
new_url = url + choose_dict(res)
print(new_url)


data = response(new_url)
soup = BeautifulSoup(data.text, 'html.parser')
results_ort = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
res = (data_extract(results_ort))
new_url2 = new_url + choose_dict(res)
print(new_url2)