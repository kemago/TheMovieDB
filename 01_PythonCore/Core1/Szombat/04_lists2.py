# lists
names = [
    'Robert',
    'Csaba'
    ]

# add item
names.append('Csilla')
names.append('Tamás')
names.append('István')
names.append('Kriszta')
names.append('Csaba')


print(names)

# indexs
print(names[1])
print(names[-1])

# remove
names.remove('Csaba')
print(names)

del names[-1]
print(names)

# a stringek is indexelhetők
my_name = 'Ágoston'
print(my_name[-1])
print(my_name[0])