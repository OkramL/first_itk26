# read_mycsv_files.py
import os

total = 0 # Kogu veeru summa
count = 0 # Loe ridu kokku

# Leia data kaustast kõik CSV failid
files = []

for filename in os.listdir('data'):
    if filename.endswith('.csv'):
        files.append(filename)

# Kuva leitud failid
print('CSV failid')

for x in range(len(files)):
    print(f'{x + 1}. {files[x]}')

# Kasutaja valib faili
file_number = int(input(f'Vali fail 1-{len(files)}: '))

if file_number >= 1 and file_number <= len(files):
    filename = 'data/' + files[file_number - 1]
    f = open(filename, 'r')
    rows = len(f.readline().split(';'))
    f.close()

    row = int(input(f'Mitmes veerg liita? 1-{rows} '))
    if row >= 1 and row <= rows:
        row -= 1 # row = row - 1
        with open(filename, 'r') as f:
            content = f.readlines()
            for line in content:
                line = line.strip()
                parts = line.split(';')
                if parts[row].isnumeric():
                    total += int(parts[row])
                    count += 1
        
        #print(total, count)
        print('Veeru summa: ' + str(total) + '.')
        print(f'Kokku loeti {count} rida.')
    else:
        print('Vigane veeru number.')
else:
    print('Vigane faili number!')