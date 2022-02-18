#########################################
# 9. Знайти набільший елемент в масиві за допомогою reduce
#     [1,6,9,0,17,88,4,7] -> 88
#########################################

current_list = [1, 6, 9, 0, 17, 88, 4, 7, 0, 88, 9, -88]
max_number = 0

for i in range(len(current_list)):
    if i+1 <= len(current_list)-1:
        if max_number < current_list[i] > current_list[i + 1]:
            max_number = current_list[i]
        elif max_number < current_list[i + 1] > current_list[i]:
            max_number = current_list[i + 1]
    else:
        print(max_number)
        break
