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

if __name__ == "__main__":
    standard_input= ''  #Behövs för ett tillägg jag använder
    url = 'https://www.klart.se'
    data = response(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    results_län = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    res = (data_extract(results_län))   #Ett lexikon som vi vill skriva ut med enumerate
    for item in res:                  
        print(f"{item:>25}: {res[item]:^15}")   #testutskrift
   

