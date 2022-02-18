#########################################
# 8. Вирівняти багаторівневий масив в однорівневий
#     [1,3, ['Hello, 'Wordd', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Wordd', 9, 6, 1, 'oops', 9]
# flat використовувати заборонено.
#########################################

current_list = [1, 3, ['Hello', 'Wordd', [9, 6, 1]], ['oops'], 9]


def fact_line_iter_proc(n):
    return fact_iter([], n)


def fact_iter(new_list, n):
    for i in n:
        if type(i) == list:
            fact_iter(new_list, i)
        else:
            new_list.append(i)
    return new_list


print(current_list)
print(fact_line_iter_proc(current_list))
