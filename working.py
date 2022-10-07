#Används av Jesper för att testa kod

#Skriver ut nycklarna i ett lexikon med ett siffervärde
def print_dict(a_dict):
    for count, key in enumerate(a_dict, start=1):   #för alla nycklar i ett lexikon
        print(f"{count}) {key}")                    #count är siffran, key är nyckeln

#Kollar om ett sifferval "selected" finns och använd dess värde
def enum_selector(a_dict, selected):
    for count, key in enumerate(a_dict, start=1):   #för alla nycklar i ett lexikon 
        if selected == str(count):                  #om siffervalet finns    
            return a_dict[key]                      #returnera värdet av den nyckeln

#Frågar om ett val och returnerar inputen
def selected():
    return input(f"Ange val:")


if __name__ == "__main__":
    standard_input = '' #Behövs för ett tillägg jag har
    test_dict = {
    'a':'värde 1', 
    'b':'värde 2',
    'c':'värde 3'
    }
    print_dict(test_dict) 
    print(enum_selector(test_dict, selected()))
