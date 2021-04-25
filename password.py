import random, string
from string import ascii_letters as letters, ascii_lowercase as low_lets, ascii_uppercase as up_lets, digits as digits_, punctuation
from random import choice
try:
    from freq import txt
except:
    txt = ''


def init(action):
    s = ''
    if action == 1:
        #Проверка пароля
        print('''Задайте критерии для проверки пароля.
Особые символы: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
Введите 0 или 1 для каждого:
''')
        t = get_params()
        s = input('Введите пароль: ')
        while s != '':
            check_pass(t, s, True)
            print('Введите 0 или пустую строку для выхода')
            s = input('Введите пароль: ')
    if action == 2:
        #Создание пароля
        print('''Задайте критерии для создания пароля (без них создастся пароль из строчных букв).
Особые символы: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
Частота особых символом в пароле меньше частоты букв и цифр
Введите 0 или 1 для каждого:
''')
        a = get_params()
        while s == '':
            print(generate(a))
            print('Введите пустую строку чтобы создать другой пароль c такими же критериями, для выхода - любой символ')
            s = input()
    if action == 3:
        print('''Задайте критерии для проверки паролей в массиве.
Особые символы: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
Введите 0 или 1 для каждого:
''')
        a = get_params()
        s = input('Введите название анализируемого файла: ')
        passs = open(s).readlines()
        passs = [i[:-1] for i in list(passs)]
        r = sum(1 if check_pass(a, i) else 0 for i in passs)
        print(f'Всего паролей: {len(passs)}')
        print(f'Соответствуют требованиям: {r}')
        print(f'Не соответствуют требованиям: {len(passs) - r}')


def get_params():
    a = [0] * 4
    a[1] = int(input('Использование прописных букв: '))
    a[2] = int(input('Использование цифр: '))
    a[3] = int(input('Использовние особых символов: '))
    a[0] = int(input('Введите длину пароля: '))
    return a


def check_pass(t, s, gen = False):
    size, upper_case, digits, special_symbols = t
    array = low_lets
    array1 = []
    issues = []
    x = True
    if len(s) != size:
        x =  False
        issues.append('Длина не соответствует заданной')
    if s.lower() in txt.lower():
        x =  False
        issues.append('Ваш пароль является одним из часто встречающихся')
    if upper_case:
        array += up_lets
        array1.append(up_lets)
    if digits:
        array += digits_
        array1.append(digits_)
    if special_symbols:
        array += punctuation
        array1.append(punctuation)
    for i in s:
        if i not in array:
            x = False
            issues.append('Использованы запрещенные символы')
            break
    met_requirements = 0
    for i in array1:
        c = 0
        for j in s:
            if j in i:
                c += 1
        if c > 0:
            met_requirements += 1
    if met_requirements != len(array1):
        issues.append('Нет требуемых символов')
        x = False
    if gen:
        print()
        if x:
            print('Пароль соответствует требованиям')
        else:
            print('Пароль не соответствует требованиям: \n')
            for i in issues:
                print(i)
        print()
    return x
    

def generate(t):
    size, upper_case, digits, special_symbols = t
    if size < sum(t[1:]):
        print()
        return 'Невозможные требования'
    array = low_lets * 10
    if upper_case:
        array += up_lets * 7
    if digits:
        array += digits_ * 7
    if special_symbols:
        array += punctuation
    ss = ''.join(choice(array) for i in range(size))
    if not check_pass(t, ss):
        return generate(t)
    else:
        return ss


print('''
Генерация и проверка паролей
Действия:
1 - проверка пароля на соответствие требованиям
2 - создания пароля по заданным критериям
3 - проверка массива паролей на соответствие критериям
''')

while True:
    print('Введите 0 или пустую строку для выхода')
    N = int(input('Выберите действие: '))
    print()
    if not N:
        break
    init(N)
    print()
    