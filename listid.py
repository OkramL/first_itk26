# listid.py
# list [nimekiri], tuple (järjend), dictonary {sõnastik}

places = [] # Tühi list
places.append('Kehtna') # Lisa listi lõppu
places.append('Rapla') # Lisa listi lõppu (peale Kehtna)
places[1:1] = ['Tallinn', 'Pärnu'] # Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisa lõppu
places.insert(2, 'Are') # Tallinn ja Pärnu vahele

numbers = [1, 7, 4, -32, 5.12, 87]

print(places)
print(numbers)
print(type(places)) # <class 'list'>
print(type(numbers[4])) # <class 'float'>

# Kustutamine
places.remove('Rapla') # Esimene mis leitakse, eemaldatakse
places.pop(6) # Viimane Rapla
del places[2] # Are
print(places)

# Ülesanne: Lisa Rapla, Pärnu ja Viljandi vahele ning listi lõppu
places.insert(3, 'Rapla')
places.append('Rapla')
print(places)

# Leiame elemendi indeksi, mitu korda seda esineb
place = places[-1] # Viimane Rapla eraldi muutujasse
index = places.index(place) # Mis indeks on esimene Rapla (3)
count = places.count(place) # Mitu Raplat leiti (2)

print(place, index, count)

if place in places:
    print(f'{place} on nimekirjas olemas.')

if 'Kohila' in places:
    print('Kohila on nimekirjas olemas!')

if 'Narva' not in places:
    print('Narvat ei leitud!')

print(len(places)) # Listi suurus
print(places[len(places)-1]) # Viimane element

# Koopia listist
list_copy = places.copy()

# Sorteerimine
list_copy.sort() # A->Z
new_list = sorted(places, reverse=True) # Z->A

print(list_copy) # Sorteeritud a->z
print(new_list) # Sorteeritud z->a
print(places) # Originaal

print() # Tühi rida

# Tühjenda list
new_list.clear()
print(new_list)

# Väljasta kolmanda elemendi keskmine täht suurtähena.
# ['Kehtna', 'Tallinn', 'Pärnu', 'Rapla', ...]
print(places[2][2].upper()) # Pärnu => R
