"""
прога, що виводить кількість кожного символа з введеної строки,
  наприклад:
  st = 'as 23 fdfdg544' #введена строка

  'a' -> 1  #вивело в консолі
  's' -> 1
  ' ' -> 2
  '2' -> 1
  '3' -> 1
  'f' -> 2
  'd' -> 2
  'g' -> 1
  '5' -> 1
  '4' -> 2
"""

from collections import Counter
st = 'as 23 fdfdg544'
for key, value in Counter(st).items():
    print(f'\'{key}\' -> {value}')
