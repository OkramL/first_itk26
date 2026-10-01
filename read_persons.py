# read_persons.py
"""
KASUTAJANIMI:
    eesnimi.perenimi
    läbivalt väikeste tähtedega
    eemaldada rõhumärgid
    eesnimes tühik ja sidekriips kaotada
EPOSTIAADRESS:
    kasutajanimi@asutus.com
KELLELE TEHA:
    Sündinud 1990 - 1999
UUS FAIL:
    Sisaldab päist
    Eesnimi;Perenimi;Isikukood;Kasutajanimi;Epost
"""
# Source - https://stackoverflow.com/a/518232
# Posted by oefe, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-01, License - CC BY-SA 3.0

import unicodedata

src = 'persons/Persons.csv'
dst = 'results/Persons_accounts.csv'
domain = '@asutus.com'
header = ['Kasutajanimi', 'EPost']

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# print(strip_accents('äöõüÄÖÕÜ àéè'))
with open(src, 'r', encoding='utf-8') as s:
    with open(dst, 'w', encoding='utf-8') as d:
        content = s.readlines()
        old_header = content[0].strip().split(';')
        new_header = ';'.join(old_header[:2] + old_header[4:] + header)

        # Kirjuta päis faili
        d.write(new_header + '\n')

        for line in content[1:]:
            parts = line.strip().split(';')
            year = int(parts[2].split('.')[2])

            if 1990 <= year <= 1999:
                first_name = parts[0]
                last_name = parts[1]

                # Eemalda eesnimest tühik ja sidekriips
                first_name = first_name.replace(' ', '')
                first_name = first_name.replace('-', '')

                # Loo kasutajanimi
                username = '.'.join([first_name, last_name]).lower()
                username = strip_accents(username)

                # E-post
                email = username + domain

                new_line = ';'.join(parts[:2] + parts[4:] + [username, email])
                d.write(new_line + '\n')