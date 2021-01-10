# my phonebook

print('=' * 50, 'My Phonebook', '=' * 50)

phonebook = {}

name = input('Name:')
phone = input('Phone:')
address = input('Address:')

phonebook[phone] = {
    'name': name,
    'address': address
}

print(phonebook)

name = input('Name:')
phone = input('Phone:')
address = input('Address:')

phonebook[phone] = {
    'name': name,
    'address': address
}

print(phonebook)