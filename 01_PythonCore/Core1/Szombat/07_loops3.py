names = [
    'Robert',
    'Csaba',
    'Tamás',
    'Kriszta',
    'Csilla'
    ]

for item in names:
    if item == 'Tamás':
        continue # kihagyja azt az egyetlen nevet, amit a feltétel tartalmaz ("skippeli")
    print(item)

print('End of code!')