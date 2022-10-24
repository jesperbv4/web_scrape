from class_klart import Klart, Klart_details, merge
from tabulate import tabulate

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

def print_table(a_list):
    col_names = labels()
    data = a_list
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

def labels():
    labels = [
        'Dag',
        'Datum',
        'Max',
        'Min',
        'Soluppgång',
        'Solnednång',
        'Regn',
        'Åska',
        'Vind',
        'Månfas',
        'UV-index',
        ]
    return labels  

def menu(details):
    options = {'Gå tillbaka':'back', 'Välj ny ort':'place', 'Avsluta':'end'}
    val = value(options)
    if val == 'back':
        menu2(details)
    elif val == 'place':
        main()
    elif val == 'end':
        return None
            

        

def menu2(details):
    options2 = {'En dag': True, '14 dagar': False, 'Avsluta': 'end'}
    val_dag = value(options2)
    if val_dag == True:
        dag = details.get_summary_day(value(details.choose_day()))
        print_table([dag])
        menu(details)
    elif val_dag == False:
        dag = details.get_summary()
        print_table(dag)
        menu(details)
    elif val_dag == 'end':
        return None
    
            
    


def main():
    page_main = Klart()
    page_ort = Klart(value(page_main.get_places()))
    details = Klart_details(value(page_ort.get_places()))
    menu2(details) 


if __name__ == "__main__":
    main()