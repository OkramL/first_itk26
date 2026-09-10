from datetime import date
# See on kommentaar

"""
See on mitmerealine
kommentaar
"""

# Muutujate omistamine
name = 'marko livental'
age = 25
height = 1.8

print(name, age, height)
# Kasutaja NAME vanuses AGEa. on pikkusega HEIGHT meetrit.
print(f'Kasutaja {name.title()} vanuses {age}a. on pikkusega {height} meetrit.')
print('Kasutaja ' + name.title() + ' vanuses ' + str(age) + 'a. ')
print('Kasutaja ' + name.title() + ' vanuses ' + str(age) + 'a. on pikkusega ' + str(height) + ' meetrit.')

# Jooksev aasta
# DD.MM.YYYY
# YYYY-MM-DD
birth_year = date.today().year - age
print(f'Sünniaasta: {birth_year}')

# print(date.today()) # YYYY-MM-DD

age = int(input('Sisesta vanus: '))

if age < 1 or age > 122:
    print('Vanus vales vahemikus. Lubatud 1-122 k.a.')
elif age < 18: # 1-17k.a
    print('Alaealine')
elif age < 65: # 18-64
    print('Tööealine')
elif age < 100: # 65-99
    print('Pensionär')
else: # 100-122 k.a.
    print('Pikaealine')

"""
küsime elukohta ja vastavalt elukoha pikkusele väljastame, 
pikk nimi, lühike nimi või viga.
Lühike nimi 2-5 märki
Pikk nimi 6+ märki
alla 2 on Viga
"""

place = input('Sisesta elukoht: ')
place = place.strip() # Eemalda algusest ja lõpust tühikud

if len(place) > 1 and len(place) <= 5:
    print(f'Lühike nimi {place}')
elif len(place) > 5:
    print(f'Pikk nimi {place}')
else:
    print('Viga')
