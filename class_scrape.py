import requests
from bs4 import BeautifulSoup

class Klart():
    def __init__(self, snippet=''):
        self.baseUrl = 'https://www.klart.se'
        self.session = requests.Session()
        self.snippet = snippet

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
  
    def get_län(self):
            return self.page().find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'}) 
   
    def get_temp(self):
        return self.page().find_all('div', attrs={'class': 'item weather'})
        
    def get_places(self):
            return [self.get_län()[i].contents[0] for i in range(len(self.get_län())-1)]

    def get_href(self):
        return [self.get_län()[i].get('href') for i in range(len(self.get_län())-1)]
    
    def temp_high(self):
        high = [int(self.get_temp()[i].find('span').find_all('span')[0].contents[0][0:-1]) for i in range(len(self.get_temp())-1)]

        if len(high) > 0:
            return high
        
    def temp_low(self):
        low = [int(self.get_temp()[i].find('span').find_all('span')[2].contents[0][0:-1]) for i in range(len(self.get_temp())-1)]

        if len(low) > 0:
            return low
            
        
        

        
    

  