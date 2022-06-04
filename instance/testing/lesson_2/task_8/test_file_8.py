login = input()
mail = input()

if '@' in login:
    print('Некорректный логин')
    exit()

if '@' not in mail:
    print('Некорректный адрес')
    exit()

else:
    print('OK')