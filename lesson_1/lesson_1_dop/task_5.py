"""
 5. Сумма цифр числа
   Дано натуральное число N. Вычислите сумму его цифр.
     При решении этой задачи нельзя использовать строки,
     списки, массивы ну и циклы, разумеется.
     Рекурсія)
"""

insert_number = int(input('Введіть N: '))


def fact_iter(n, counter=0):
    counter += n % 10
    n //= 10

    if n:
        return fact_iter(n, counter)
    return counter


print(fact_iter(insert_number))
