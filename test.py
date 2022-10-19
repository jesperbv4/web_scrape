from sympy import det
from class_scrape import Klart, Klart_details


def indexify(dict):
    y = enumerate(dict, start=1)
    return y

def print_index(dict):
    for index, key in indexify(dict):
        print(f"{index}) {key}")

def value(dict):
    print_index(dict)
    while True:
        selected = select()
        for index, key in indexify(dict):
            if selected == str(index) or selected.capitalize() == key:
                return dict[key]

def select():
    return input("Option: ")


def main():
    page_main = Klart()
    page_ort = Klart(value(page_main.get_places()))
    details = Klart_details(value(page_ort.get_places()))
    print(details.get_summary(2))
    print(details.get_temphigh())
   
    



    # page = Klart_details('/se/uppsala-län/väder-uppsala/')
    # print(page.get_temphigh(),)


if __name__ == "__main__":
    main()