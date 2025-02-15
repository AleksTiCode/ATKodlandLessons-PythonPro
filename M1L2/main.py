import random

list = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = {}

while True:
    mode = int(input('Выберите режим (0 - добавить пароль, 1 - вывести пароли)'))
    if mode == 0:
        len_pass = input("Введите длину пароля:")
        name_pass = input('Имя переменной:')

        password[name_pass] = ''
        for i in range(int(len_pass)):
            password[name_pass] = random.choice(list) + password[name_pass]
        
        print(password[name_pass])
        print('Переменная добавлена')
    elif mode == 1:
        print('Вывод паролей:')
        for i in password:
            print(i, password[i])
    else:
        print('Такого нету')