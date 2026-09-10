# for_loop.py
from random import randint

names = ['Mari', 'Anna', 'Villem', 'Jüri']

# Väljasta kõik nimed nimekirjast
for name in names:
    print(name)

print() # Tühi rida

for x in range(4):
    print(names[x], end=' ') # Ühel real tühik vahel

print('\n') # Kaks reavahetust

for x in range(1, 5):
    print(x, end=' | ')

print('\n')

for x in range(0, 10, 2):
    print(x, end='|')

print('\n')

# while-loop
x = 0
while x < len(names):
    print(names[x], randint(1, 122))
    x += 1 # x = x + 1
print()

# ÜLESANNE: Väljasta listi nimed konsooli iga nimi 
# eradli real. Iga nimi algab järjekorra numbriga
# ja kasvavalt. Järjekorra numbri järgi on punkt ja 
# tühik enne nime:
# 1. Mari
# 2. Anna
# ....
for x in range(len(names)):
    # print(str(x+1) + '. ' + names[x])
    print(f'{x+1}. {names[x]}')

print()

# Sama mis eelmine
x = 1
while x <= len(names):
    print(f'{x}. {names[x-1]}')
    x += 1
