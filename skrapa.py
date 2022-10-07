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

if __name__ == "__main__":
    standard_input= ''  #Behövs för ett tillägg jag använder
    data = req_with_cookie(get_cookie_playwright())
    soup = BeautifulSoup(data.text, 'html.parser')
    results_län = soup.find('div', attrs={'class':'link-list'}).find_all('a', attrs={'class': 'link'})
    res = (data_extract(results_län))   #Ett lexikon som vi vill skriva ut med enumerate
    for item in res:                  
        print(f"{item:>25}: {res[item]:^15}")   #testutskrift
   

""" Du kan behöva importera playwright
    Kör: pip install playwright         """
