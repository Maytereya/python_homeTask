import ast

path = 'phone.txt'  # Файл с контактами
collect = dict()  # Словарь с данными отдельного контакта
phonebook = list()  # Cписок со словарями - данными отдельных контактов

number = 0  # Порядковый номер контакта со значением по умолчанию, нужен для изменения контакта.
found = False # Флаг для корректной работы замены.


def add_contact(f, ph, n):
    collect["Имя"] = f
    collect["Телефон"] = ph
    collect["Заметка"] = n
    with open(path, 'a') as add_data:
        add_data.write(f'{collect}\n')


def print_contacts():
    with open(path, 'r') as add_data:
        lines = add_data.readlines()
        for line in lines:
            phonebook.append(line.rstrip())


def search_contact(in_sr4: str):
    print_contacts()
    for j in range(len(phonebook)):
        if in_sr4 in phonebook[j]:
            tmp = ast.literal_eval(phonebook[j])
            print('=================')
            print(f"# {j + 1}")
            for itm in tmp.values():
                print(f"{itm}")


print('\tДобавить контакт: 1\n \tВывести все контакты: 2\n \tНайти контакт: 3\n \tРедактировать контакт: 4\n')
io = input('Введите номер команды: ')

if io == '1':
    print('Добавить контакт')
    fio = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    note = input('Введите комментарий: ')
    add_contact(fio, phone, note)

elif io == '2':
    print_contacts()
    print('Вывод на экран всего справочника')
    for i in range(len(phonebook)):
        print('#', i + 1)
        temp = ast.literal_eval(phonebook[i])
        for k, v in temp.items():
            print(f'\t{k}: {v}')
        print('===========================')

elif io == '3':
    print('Поиск в телефонном справочнике')
    in_search = input('Искать: ')
    search_contact(in_search)

elif io == '4':
    print_contacts()
    print('Найти и изменить контакт в телефонной книге')
    in_search = input('Search: ')

    for i in range(len(phonebook)):
        if in_search in phonebook[i]:
            found = True
            number = i
            print(f"Порядковый номер контакта: {i + 1}")
            temp = ast.literal_eval(phonebook[i])
            for item in temp.values():
                print(f"{item}")

    if found:
        change = input("Изменить контакт? Y/N: ")
        if change == 'Y':
            fio = input(f"Измените имя: ")
            phone = input('Измените номер телефона: ')
            note = input('Измените комментарий: ')

            phonebook[number] = '{' + '"Имя": ' + '"' + fio + '"' + ', ' + '"Телефон": ' + '"' + \
                                phone + '"' + ', ' + '"Заметка": ' + '"' + note + '" ' + '}'

            with open(path, 'w') as write_data:
                for i in range(len(phonebook)):
                    write_data.write(f'{phonebook[i]}\n')
        else:
            print("Ни один из контактов не изменен")
    else:
        print("Контакт не найден")
