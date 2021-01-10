age = 10

if age > 10:
    print('You are older than me!')
elif age == 10:
    print('We have the same age.')
else:
    print('You are younger than me!')

# egyéb relációs jelek
# <=
# >=
# !=

username = 'Robert'
password = 'testpas123'

your_user = input('username: ')
your_password = input('password: ')

if username == your_user and password == your_password:
    print('You are logged in!')
else:
    print('Invalid credentials provided. Try again.')