# dictionary = asszociatív tömb :)

my_list = ['Robert', 52, 3.14]
#             kulcs   érték     kulcs   érték kulcs érték
phonebook1 = {'name': 'Robert', 'number': 52, 'pi': 3.14}
print(phonebook1['name'])

phonebook = {
    'name': 'Ágoston Kemenesi',
    'phone': '06 20 555 6666',
    'address': "Debrecen, Fő u. 1.",
    "my_list": my_list
}

print(phonebook['name'])
print(phonebook['phone'])
print(phonebook['address'])
print(phonebook['my_list'])

phonebook2 = {
    'name': 'Ágoston Kemenesi',
    'phone': '06 20 555 6666',
    'address': "Debrecen, Fő u. 1.",
    'name': 'Robert Vari', # nem lehet két azonos kulcs
    'data': ['egyik', 'masik']
}

print(phonebook2['name'])

# megoldás a kulcsazonosságra
# "fő-kulcs" (root key) megadása és utána egy hagyományos dictionary
phonebook3 = {
    '06 20 255 6666': {
        'name': 'Ágoston Kemenesi',
        'address': "Debrecen, Fő u. 1.",
    },
    '06 30 111 3333': {
        'name': 'Csaba Nagy',
        'address': "Győr, Kossuth u. 1.",
    }
}

# add item to dictionary
phonebook3['06 70 111 222'] = {
    'name': 'Kovács Péter',
    'address': "Eger, Főbb u. 1."
}

print(phonebook3)

# ugyanígy írunk felül adatot (override)

print(
    phonebook3['06 30 111 3333']['name'],
    phonebook3['06 20 255 6666']['name']
)

# delete item
del phonebook3['06 70 111 222']
print((phonebook3))
