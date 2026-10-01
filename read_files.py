# read_files.py
"""
Loeme faili names.txt. Kontrollime kas fail on olemas ja
sisaldab ka sisu. Uude faili kirjutame nimi, juhusliku vanuse
ja juhusliku kuupäeva ja kellaaja jooksval kuul.
"""
from datetime import datetime
from random import randint
from calendar import monthrange
from os.path import exists, getsize

names_filename = 'results/names.txt'
persons_filename = 'results/persons.txt'

# Kontrolli kas nimede fail on olemas
if exists(names_filename):
    # Kontrollime kas failis on sisu
    if getsize(names_filename) > 0:
        # Tänane kuupäev
        now = datetime.now()

        # Jooksva kuu päevade arv
        days_in_month = monthrange(now.year, now.month)[1]
        
        # Avame faili lugemiseks
        with open(names_filename, 'r', encoding='utf-8') as src:
            # Avame uue faili ülekirjutamiseks
            with open(persons_filename, 'w', encoding='utf-8') as dst:
                # Töötleme faili reakaupa
                for line in src:
                    name = line.strip()
                    # Juhuslik vanus
                    age = randint(1, 122)
                    # Juhuslik kuupäev ja kellaaeg (jooksev kuu)
                    random_date = datetime(
                        now.year, 
                        now.month, 
                        randint(1, days_in_month), 
                        randint(0, 23), 
                        randint(0, 59), 
                        randint(0, 59)
                    )
                    # Kuupäeva vormindamine
                    date_time = random_date.strftime('%d.%m.%Y %H:%M:%S')
                    # print(name, age, date_time)
                    # Kirjutame faili
                    # dst.write(f'{name};{age};{date_time}\n')
                    person = [name, str(age), date_time]
                    dst.write(';'.join(person) + '\n')

                
                print(f'Fail {persons_filename} loodud.')
    else:      
        print(f'Fail {names_filename} on tühi.')
else:
    print(f'Faili {names_filename} ei leitud.')