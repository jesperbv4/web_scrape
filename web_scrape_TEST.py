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

def extract(url, _class):
    return scraper(url).find_all(attrs={'class': _class})

def compile_dict(scrape, find, index1, index2):
    return [scrape[i].find_all(find)[index1].contents[index2] for i in range(len(scrape))]

# Skapar en dictionary med dagen och datumet som key och en ny dictionary som value. 
# Denna dictionary innehåller bl.a. max temp, min temp, nederbörd och vindstyrka
def temp_extract(url):
    scrape_details = extract(url, 'details visible-medium-up') 
    data_dict = {}
    for n in range(len(scrape_details)):
        day = scrape_details[n].find_all(attrs={'class': 'long'})[0].contents[0]
        date = scrape_details[n].find_all(attrs={'class': 'item time'})[0].contents[0]
        temp_high = scrape_details[n].find_all(attrs={'aria-label': 'Max temperatur'})[0].contents[0]
        temp_low =  scrape_details[n].find_all(attrs={'aria-label': 'Min temperatur'})[0].contents[0]
        sun_up = scrape_details[n].find(attrs={'class': 'item sun-times'}).find_all('span')[0].contents[0]
        sun_down = scrape_details[n].find(attrs={'class': 'item sun-times'}).find_all('span')[1].contents[0]

        data_dict[day+date] = {'Max temp': temp_high, 'Min tem': temp_low, 'Soluppgång': sun_up, 'Solnedgång': sun_down}
        
        scrape_row = scrape_details[n].find_all(attrs={'class': 'row'})
        
        for x in range(len(scrape_row)):
            data_dict[day+date][scrape_row[x].find_all('span')[0].contents[0]] = scrape_row[x].find_all('span')[1].contents[0]
    return data_dict
    
def indexify(dict):
    y = enumerate(dict, start=1)
    return y

def print_index(dict):
    for index, key in indexify(dict):
        print(f"{index}) {key}")

def choose_dict(dict):
    print_index(dict)
    print('\nr) Return\n')
    while True:
        selected = select()
        for index, key in indexify(dict):
            if selected == 'r':
                return dict
            elif selected == str(index) or selected.capitalize() == key:
                return dict[key]

def select():
    return input("Option: ")

def new_page(url):
    res = (data_extract(url))
    snippet = choose_dict(res)
    return snippet


# def display_temp(list):
#     for i in range(len(list)):
#         print(f'\n{list[i][0].capitalize()} {list[i][1]}:')
#         print(f'    Max temp: {list[i][2]}°\n    Min temp: {list[i][3]}°')

def menu(options, prompt):
    print()
    for o in options:
        print(f"{o}) {options[o]}")
    print()
    while True:
        option = input(prompt)
        if option in options:
            print()
            return option
        else:
            continue

def user_actions(options, prompt):
    opt = menu(options, prompt)
    for index, key in options:
        if opt == index or opt == key:
            return key
        
             




def main():
    url = 'https://www.klart.se'
    print('\nVälj län:\n')
    län = url + new_page(url)
    print('\nVälj ort:\n')
    ort = url + new_page(län)
    all_data = temp_extract(ort)
    print('\nVälj dag\n')
    dag = choose_dict(all_data)
    print('\nVad vill du se?\n')
    data = choose_dict(dag)
    print(f'\n{data}\n')
    print('\nVad vill du göra?\n')
    options = {'Gå tillbaka':'back', 'Välj ny dag':'day', 'Välj ny ort':'place', 'Avsluta':'end'}
    val = choose_dict(options)
    while True:
        if val == 'back':
            data = choose_dict(dag)
            print(f'\n{data}\n')
            print('\nVad vill du göra?\n')
            val = choose_dict(options)
        elif val == 'day':
            print('\nVälj dag\n')
            dag = choose_dict(all_data)
            print('\nVad vill du se?\n')
            data = choose_dict(dag)
            print(f'\n{data}\n')
            print('\nVad vill du göra?\n')
            val = choose_dict(options)
        elif val == 'place':
            url = 'https://www.klart.se'
            print('\nVälj län:\n')
            län = url + new_page(url)
            print('\nVälj ort:\n')
            ort = url + new_page(län)
            all_data = temp_extract(ort)
            print('\nVälj dag\n')
            dag = choose_dict(all_data)
            print('\nVad vill du se?\n')
            data = choose_dict(dag)
            print(f'\n{data}\n')
            print('\nVad vill du göra?\n')
            options = {'Gå tillbaka':'back', 'Välj ny dag':'day', 'Välj ny ort':'place', 'Avsluta':'end'}
            val = choose_dict(options)
        elif val == 'end':
            return None






if __name__ == "__main__":
    main()

# print(choose_dict(choose_dict(temp_extract('https://www.klart.se/se/uppsala-l%C3%A4n/v%C3%A4der-uppsala/'))))

