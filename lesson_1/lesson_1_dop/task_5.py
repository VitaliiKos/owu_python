#########################################
# 5. Сумма цифр числа
#   Дано натуральное число N. Вычислите сумму его цифр.
#     При решении этой задачи нельзя использовать строки,
#     списки, массивы ну и циклы, разумеется.
#     Рекурсія)
#########################################

insert_number = int(input('Введіть N: '))


def fact_line_iter_proc(n):
    return fact_iter(0, n)


def fact_iter(counter, n):
    counter += n % 10
    n //= 10
    if n == 0:
        return counter
    else:
        return fact_iter(counter, n)


print(fact_line_iter_proc(insert_number))
