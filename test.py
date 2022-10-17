from class_scrape import Klart

def merge(a, b, list=False, dict=False, tuple=False):
        if dict == True:
            return {a[i]: b[i] for i in range(len(a))}
        elif list == True:
            return [[a[i], b[i]] for i in range(len(a))]
        elif tuple == True:
            return [(a[i], b[i]) for i in range(len(a))]
        else: 
            return None


def indexify(dict):
    y = enumerate(dict, start=1)
    return y

def print_index(dict):
    for index, key in indexify(dict):
        print(f"{index}) {key}")

def choose_dict(dict):
    print_index(dict)
    while True:
        selected = select()
        for index, key in indexify(dict):
            if selected == str(index) or selected.capitalize() == key:
                return dict[key]

def select():
    return input("Option: ")

def new_page(snippet=''):
    page = Klart(snippet)
    return page

def main():
    page = new_page()
    län = new_page(choose_dict(merge(page.get_places(), page.get_href(), dict=True)))
    ort = new_page(choose_dict(merge(län.get_places(), län.get_href(), dict=True)))
    temp = merge(ort.temp_high(), ort.temp_low(), tuple=True)
    print(temp)


    

if __name__ == "__main__":
    main()