"""
2. Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
 Всегда будет только одно целое число, которое встречается нечетное количество раз
     [1,2,3,4,5,2,4,1,3] -> 5
"""

current_list = [1, 2, 3, 4, 5, 2, 4, 1, 3, 4]

for i in current_list:
    count_number = current_list.count(i)
    if count_number % 2 != 0:
        print('number:', i, '-> count:', count_number)
        break
