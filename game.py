# game.py
"""
Arvuti mõeldud number on vahemikus 1-100 k.a.
Loendame samme. Mäng lõpeb kui on sisestatud 
õige number.

TÄIENDUS: Kui mäng saab läbi, siis küsi kasutajalt
kas mängida veel? Kui Jah (j/J), siis reseti andmed
ja alusta uut mängu.
"""
from random import randint

pc_nr = randint(1, 100)
steps = 0
game_over = False

# print(pc_nr)

def ask():
    """Küsib mängijalt arvu ja kontrollib vastust"""

    global steps, game_over
    user_nr = int(input('Sisesta number [1-100]: '))
    steps += 1 # steps = steps + 1

    if user_nr == 1000:
        print('Leidsid tagaukse. Õige number on ' + str(pc_nr))
    elif user_nr > pc_nr:
        print('Väiksem')
    elif user_nr < pc_nr:
        print('Suurem')
    elif user_nr == pc_nr:
        print(f'Arvasid numbri ära {steps} sammuga.')
        game_over = True

    return game_over

def lets_play():
    """Käivitab äraarvamise mängu"""
    global pc_nr, steps, game_over

    while not game_over:
        ask()

    answer = input('Kas mängida veel? [J/E] ')
    if answer in ['J', 'j']: # answer.lower() == 'j'
        pc_nr = randint(1, 100)
        steps = 0
        game_over = False
        lets_play()

lets_play()
print('Mäng on läbi.')
