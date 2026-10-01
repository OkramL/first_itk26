# files.py
filename = 'results/name.txt'
names_filename = 'results/names.txt'

def valid_name(name):
    """Kontrollib, kas nimi on sobiv"""

    if len(name) < 2:
        return False

    for char in name:
        if not char.isalpha() and char != " " and char != "-":
            return False

    return True
    

name = input('Sisesta oma nimi: ')

file = open(filename, 'w', encoding='utf-8') 
file.write(name)
file.close() # Faili sulgemine

print(f'Nimi {name} salvestati faili {filename}.')

if valid_name(name):
    with open(names_filename, 'a', encoding='utf-8') as file:
        file.write(name + '\n') # nimi ja reavahetus
    
    print(f'Nimi {name} lisati faili {names_filename}.')
else:
    print(f'Nime {name} ei lisatud faili!')