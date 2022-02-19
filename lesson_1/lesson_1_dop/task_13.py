"""
генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
задача сделать c него лист листов такого плана:

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [[1], [3, 5], [7, 9, 11], [13,15,17,19]]
[1, 3, 5, 7, 9, 11]                  => [[1], [3, 5], [7, 9, 11]]
[1, 3, 5, 7, 9]                      => [[1], [3, 5], [7, 9]]
[1, 3, 5, 7, 9, 11, 13]              => [[1], [3, 5], [7, 9, 11], [13]]
"""

n = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
k = [1, 3, 5, 7, 9, 11]
m = [1, 3, 5, 7, 9]
g = [1, 3, 5, 7, 9, 11, 13]

list_lists = [n, k, m, g]

for j in list_lists:
    i = 1
    new_list = []
    while len(j):
        new_list.append(j[:i])
        del j[:i]
        i += 1
    print(new_list)
