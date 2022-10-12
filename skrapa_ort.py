import requests
from bs4 import BeautifulSoup


def response(url):
    url = url
    s = requests.Session()
    r = s.get(url)
    return r


def data_extract(results):
    cities = [results[i].contents[0] for i in range(len(results)-1)]  
    links = [results[i].get('href') for i in range(len(results)-1)]
    res = {cities[i]: links[i] for i in range(len(cities))}
    return res


def skrapa_ort(url):
    data = response(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    results_lan = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    res = (data_extract(results_lan))   #Ett lexikon som vi vill skriva ut med enumerate
    return res


def temp_extract(url):
    data = response(url)
    soup = BeautifulSoup(data.text, "html.parser")
    results = soup.find_all('div', attrs={'class': 'item weather'})
    temp_high = [int(results[i].find('span').find_all('span')[0].contents[0][0:-1]) for i in range(len(results)-1)]
    temp_low =  [int(results[i].find('span').find_all('span')[2].contents[0][0:-1]) for i in range(len(results)-1)]
    temp = [(temp_high[i], temp_low[i]) for i in range(len(temp_high))]
    return temp


def test_print(a_dict):
    for index, item in enumerate(a_dict, start=1):                  
        print(f"{index:>20} {item:<12}: {a_dict[item]:^15}")   #testutskrift


if __name__ == "__main__":
    standard_input= ''  #Behövs för ett tillägg jag använder
    url = 'https://www.klart.se/se/uppsala-l%C3%A4n/v%C3%A4der-uppsala/'
    temp_extract(url)
