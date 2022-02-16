####################################################
# List
####################################################
# 1)Дан лист: list = [22, 3,5,2,8,2,-23, 8,23,5]

# List Task 1. найти min число в листе
list_task1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(list_task1)
print('List Task-1.1:', min(list_task1))
print('---------------------------------')

# List Task 2. удалить все дубликаты в листе
list_task_2 = list_task1[:]
result_list = []
for i in list_task_2:
    if i not in result_list:
        result_list.append(i)
print(list_task1)
print('List Task-1.2:', result_list)
print('---------------------------------')

# List Task 3. заменить каждое четвертое значение на "Х"
list_task_3 = list_task1[:]
for j in range(3, len(list_task_3), 4):
    list_task_3[j] = "X"
print(list_task1)
print('List Task-1.3:', list_task_3)
print('---------------------------------')

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
square = input('Task-2. Insert side square:')
if not square.isdigit() or int(square) <= 0:
    print('Wrong data!')
elif int(square):
    if int(square) == 1:
        print('*')
    else:
        print("*" * int(square))
        for i in range(int(square) - 2):
            print(f'*{(int(square) - 2) * " "}*')
        print("*" * int(square))
print('---------------------------------')

# 3) вывести табличку умножения с помощью цикла while
start_number = 1
print('Task-3')
while start_number <= 9:
    second_start_number = 1
    while second_start_number <= 9:
        print(f'{str(start_number * second_start_number).center(2)}', end=' ')
        second_start_number += 1
    print()
    start_number += 1
print('---------------------------------')
