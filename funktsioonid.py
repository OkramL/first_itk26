# funktsioonid.py
def welcome():
    print('Tere, kuidas läheb?')

def welcome_name(name):
    return f'Tere, {name}!'

def division(number1, number2):
    """Teostab kahe arvu jagamist"""
    if number2 != 0:
        return number1 / number2
    return -1

def introduce(name, age=25):
    """
    Loob lihtsa tutvustava lause

    :param name: str Isiku nimi
    :param age: int Isiku vanus (vaikimisi 25)
    :return: Tekstiline tutvustus vormis
            'Tema on <name> ja ta on <age> aastane!'
    :rtype: string
    """
    return f'Tema on {name} ja ta on {age} aastane!'

for x in range(5):
    welcome()

print(welcome_name('Marko'))

names = ['Jüri', 'Mari', 'Ants', '', '  Anna ']
for nimi in names:
    print(welcome_name(nimi))

print(division(5, 2))
print(division(5, 0))
result = division(10, len(names))
print(result, len(names))

print(introduce('Marko', 19))
print(introduce('Mari'))
print(introduce(1234, 567))
print(introduce(89))
print(introduce(age=99, name='Anna-Maria'))

"""
Väljasta kõik nimed listist names, mis on täpselt 
4 märki pikad.
"""
for name in names:
    if len(name.strip()) == 4:
        print(name.strip())