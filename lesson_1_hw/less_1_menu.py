# 4) переделать первое задание под меню с помощью цикла

list_task = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def menu_option_1():
    print('------------------------------------------------')
    print(list_task)
    print('List Task-1:', min(list_task))
    print('------------------------------------------------')


def menu_option_2():
    result_list_menu = []
    for i in list_task:
        if i not in result_list_menu:
            result_list_menu.append(i)
    print('------------------------------------------------')
    print(list_task)
    print('List Task-2:', result_list_menu)
    print('------------------------------------------------')


def menu_option_3():
    list_task_3 = list_task[:]
    for i in range(3, len(list_task_3), 4):
        list_task_3[i] = "X"
    print('------------------------------------------------')
    print(list_task_3)
    print('List Task-3:', list_task_3)
    print('------------------------------------------------')


def menu_option_4():
    result = None
    mean_number = sum(list_task)/len(list_task)
    for i in list_task:
        if result is None:
            result = i
        elif abs(mean_number - i) < abs(mean_number - result):
            result = i
    print('------------------------------------------------')
    print('Середнє арифметичне: ', mean_number)
    print('Елемент, значення якого найближче до середнього арифметичного: ', result)
    print('------------------------------------------------')


def menu_option_5():
    start_number_menu = 1
    print('------------------------------------------------')
    while start_number_menu <= 9:
        for i in range(1, 10):
            print(f'{str(i * start_number_menu).center(2)}', end=' ')
        print()
        start_number_menu += 1
    print('------------------------------------------------')


def main():
    while True:
        print('1. найти min число в листе.')
        print('2. удалить все дубликаты в листе.')
        print('3. заменить каждое четвертое значение на "Х".')
        print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех.')
        print('5. вывести табличку умножения с помощью цикла while.')
        print('6. Выход')
        menu_number = input('Зробіть свій вибір:')
        if not menu_number.isdigit() or 0 >= int(menu_number) > 6:
            print('------------------------------------------------')
            print('Wrong number!')
            print('------------------------------------------------')
        else:
            if int(menu_number) == 1:
                menu_option_1()
            elif int(menu_number) == 2:
                menu_option_2()
            elif int(menu_number) == 3:
                menu_option_3()
            elif int(menu_number) == 4:
                menu_option_4()
            elif int(menu_number) == 5:
                menu_option_5()
            elif int(menu_number) == 6:
                break
            else:
                print('------------------------------------------------')
                print("Wrong number!")
                print('------------------------------------------------')


if __name__ == '__main__':
    main()
