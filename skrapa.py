from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup

def get_cookie_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.klart.se/")
        cookie_for_request = context.cookies()[9]['value']
        browser.close()
        print(cookie_for_request)

def req_with_cookie(cookie_for_request, snippet=""):
    cookies = dict(
        Cookie=f'__glmrid=34c3a78b-c59f-478d-a8b3-1f1e35329bf7; LAST_PLACES_UPDATED_0.0.1=1; Glimr=; _sp_v1_uid=1:380:8d760f45-547a-4b8e-9968-f8e594a87d01; _sp_v1_data=2:489630:1664987530:0:1:0:1:0:0:_:-1; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKRmbkgRiGtbE6MUqpIGZeaU4OkF0CVlBdi1tCKRYALEldIlIAAAA%3D; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; consentUUID={cookie_for_request};')
    r = requests.get(f"https://www.klart.se/{snippet}")
    return r

def data_extract(results):
    print(len(results))
    cities = [results[i].contents[0] for i in range(len(results)-1)]  
    links = [results[i].get('href') for i in range(len(results)-1)]
    res = {cities[i]: links[i] for i in range(len(cities))}
    return res


#Skriver ut nycklarna i ett lexikon med ett siffervärde
def print_dict(a_dict):
    for count, key in enumerate(a_dict, start=1):   #för alla nycklar i ett lexikon
        print(f"{count:>5}) {key}")                    #count är siffran, key är nyckeln

#Kollar om ett sifferval "selected" finns och använd dess värde
def selector(a_dict, selected):
    for count, key in enumerate(a_dict, start=1):   #för alla nycklar i ett lexikon 
        if selected == str(count):                  #om siffervalet finns    
            return a_dict[key]                      #returnera värdet av den nyckeln

#Frågar om ett val och returnerar inputen
def selected():
    return input(f"Ange val:")
    

if __name__ == "__main__":
    standard_input= ''
    data = req_with_cookie(get_cookie_playwright())
    soup = BeautifulSoup(data.text, 'html.parser')
    results_län = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'}) #22 element av värde
    res = (data_extract(results_län)) 
    print_dict(res)
    print(selector(res, selected()))
   
    
