xs = {"a":"Värde 1", "b":"Värde 2", "c":"Värde 3"}



def indexify(dict):
    y = enumerate(dict, start=1)
    return y

def print_index(dict):
    for index, key in indexify(dict):
        print(f"{index}) {key}")

def choose_dict(dict):
    print_index(dict)
    while True:
        selected = int(select())
        for index, key in indexify(dict):
            if selected == index:
                return dict[key]

def select():
    return input("Option: ")



choose_dict(xs)