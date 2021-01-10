username = 'Robert'
password = 'testpas123'

your_username = input('username:')


while your_username != username:
    print('Username is invalid')
    your_username = input('username:')

your_password = input('password:')
while your_password != password:
    print('Password is invalid')
    your_password = input('password:')

print(f'You are logged in {username}.')