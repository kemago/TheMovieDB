# String method-ok (a string is egy object)
# upper()
print('Hello World!'.upper())

# lower()
print('Hello World!'.lower())

# title()
print('kemenesi ágoston'.title())

# replace
print('Hello World!'.replace('l', 'X'))
print('Hello World!'.replace('World', 'Ágoston'))

# együtt
print('hello world'.title().replace('o', '0').center(50, '='))

# format
# print('{} {}').format('Hello', 'World')) # place holder karakterek
# előre nem ismert adatok kiírásának előkészítésére
print("My name is {}. I'm {} years old.".format('Kemenesi Ágoston', 52))

# formated string (ugyanaz, mint a fenti, csak modernebben)
print(f"My name is {'Ágoston'}. I'm {52} years old.")