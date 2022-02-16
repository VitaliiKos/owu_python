"""
    - створити пустый список users_list = []
    - стврорити меню в якому потрібно реалізувати:

    1) додававання нового юзера
    2) вивід всіх юзерів
    3) вивід всіх юзерів за віком
    4) видалення юзера по id
    5) заміна статуса юзера на протилежний
    6) вихід з меню

    приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}
"""

users_list = []


def add_user():
    name = input('Введіть Ім\'я: ')
    age = input('Введіть вік: ')
    status = input('Введіть статус: ')

    users_list.append({'id': 0 if len(users_list) == 0 else users_list[-1]['id'] + 1, 'name': name, 'age': int(age),
                       'status': True if status == 'True' else False})

    print('------------------------------------------------')
    print(f'Користувача {users_list[-1]} додадно')
    print('------------------------------------------------')


def get_all_users():
    print('------------------------------------------------')
    if len(users_list):
        for i in users_list:
            print(i)
    else:
        print('Список користувачів пустий.')
    print('------------------------------------------------')


def get_by_age():
    sorted_users_by_age = sorted(users_list, key=lambda d: d['age'])

    print('------------------------------------------------')
    print(sorted_users_by_age)
    print('------------------------------------------------')


def delete_user_by_id():
    user_id = int(input('Введіть id: '))

    for i in users_list:
        if user_id == i['id']:
            users_list.remove(i)
            print('------------------------------------------------')
            print(f'Користувач {i} видалений.')
            print('------------------------------------------------')
            break
    else:
        print('------------------------------------------------')
        print('Такий користувач відсутній в списку!  ')
        print('------------------------------------------------')


def change_status():
    user_id = int(input('Введіть id для зміни статусу: '))

    for i in users_list:
        if user_id == int(i['id']):
            print('------------------------------------------------')
            print('Статус користувача :', i['status'])
            i['status'] = not i['status']
            print('Статус зміненно на :', i['status'])
            print('------------------------------------------------')
            break
    else:
        print('------------------------------------------------')
        print('Такий користувач відсутній в списку!  ')
        print('------------------------------------------------')


def main():
    while True:
        print('1. Додати нового юзера.')
        print('2. Вивід всіх юзерів.')
        print('3. Вивід всіх юзерів за віком.')
        print('4. Видалити юзера по id.')
        print('5. заміна статуса юзера на протилежний.')
        print('6. Вихід')

        menu_number = input('Зробіть свій вибір:')

        if menu_number == '1':
            add_user()
        elif menu_number == '2':
            get_all_users()
        elif menu_number == '3':
            get_by_age()
        elif menu_number == '4':
            delete_user_by_id()
        elif menu_number == '5':
            change_status()
        elif menu_number == '6':
            break
        else:
            print('------------------------------------------------')
            print("Wrong number!")
            print('------------------------------------------------')


if __name__ == '__main__':
    main()
