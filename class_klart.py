import requests
from bs4 import BeautifulSoup

class Klart():
    def __init__(self, snippet=''):
        self.baseUrl = 'https://www.klart.se'
        self.session = requests.Session()
        self.snippet = snippet
        self.soup = self.page()

    def url(self):
        return self.baseUrl + self.snippet

    def response(self):
        response = self.session.get(self.url())
        return response

    def parse(self):
        return BeautifulSoup(self.response().text, 'html.parser')
        
    def page(self, hidden=True):
        page = self.parse()
        if hidden == False:
            print(page)
            return(page)
        return page    
  
    def get_places(self):
        data = self.soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
        places = [data[i].contents[0] for i in range(len(data)-1)]
        href = [data[i].get('href') for i in range(len(data)-1)]
        return merge(places, href, dict=True)
   

class Klart_details():
    def __init__(self, snippet):
        self.baseUrl = 'https://www.klart.se'
        self.session = requests.Session()
        self.snippet = snippet
        self.soup = self.page()
        self.data = self.extract_data()
        

    def url(self):
        return self.baseUrl + self.snippet

    def response(self):
        response = self.session.get(self.url())
        return response

    def parse(self):
        return BeautifulSoup(self.response().text, 'html.parser')
        
    def page(self, hidden=True):
        page = self.parse()
        if hidden == False:
            print(page)
            return(page)
        return page  
    
    def extract_data(self):
        data = self.soup.find_all(attrs={'class': 'details visible-medium-up'})
        return data

    def get_day(self, n=-1):
        day = [self.data[i].find_all(attrs={'class':'long'})[0].contents[0] for i in range(len(self.data))]
        return day
    
    def get_date(self):
        date = [self.data[i].find_all(attrs={'class': 'item time'})[0].contents[0] for i in range(len(self.data))]
        return date

    def get_temphigh(self, n=-1):
        temp_high = [self.data[i].find_all(attrs={'aria-label': 'Max temperatur'})[0].contents[0] for i in range(len(self.data))]
        if n >= 0:
            return temp_high[int(n)]
        else:
            return temp_high

    def get_templow(self):
        temp_low = [self.data[i].find_all(attrs={'aria-label': 'Min temperatur'})[0].contents[0] for i in range(len(self.data))]
        return temp_low

    def get_sunup(self):
        sun_up = [self.data[i].find(attrs={'class': 'item sun-times'}).find_all('span')[0].contents[0] for i in range(len(self.data))]
        return sun_up

    def get_sundown(self):
        sun_down = [self.data[i].find(attrs={'class': 'item sun-times'}).find_all('span')[1].contents[0] for i in range(len(self.data))]
        return sun_down
    
    def get_rain(self):
        rain = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[1].contents[0] for i in range(len(self.data))]
        return rain
        
    def get_chance_of_rain(self):
        chance_of_rain = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[3].contents[0] for i in range(len(self.data))]
        return chance_of_rain

    def get_wind(self):
        wind = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[5].contents[0] for i in range(len(self.data))]
        return wind

    def get_thunder(self):
        thunder = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[7].contents[0] for i in range(len(self.data))]
        return thunder

    def get_moon(self):
        moon = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[9].contents[0] for i in range(len(self.data))]
        return moon

    def get_uv_index(self):
        uv_index = [self.data[i].find(attrs={'class': 'details'}).find_all('span')[11].contents[0] for i in range(len(self.data))]
        return uv_index

    def get_summary(self, n):
        return {'Datum': self.get_date(), 'Max': self.get_temphigh(n)}


def merge(a, b, list=False, dict=False, tuple=False):
    if dict == True:
        return {a[i]: b[i] for i in range(len(a))}
    elif list == True:
        return [[a[i], b[i]] for i in range(len(a))]
    elif tuple == True:
        return [(a[i], b[i]) for i in range(len(a))]
    else: 
        return None
            
        
        

        
    

  