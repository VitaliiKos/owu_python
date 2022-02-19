"""
вивести послідовність Фібоначі, кількість вказана в знінній,
  наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
  (число з послідовності - це сума попередніх двох чисел)

"""
x = int(input('Insert number: '))

fib1 = fib2 = 1
print(f'x = {x} -> ', end=' ')
if x < 0:
    print("Incorrect input entered")
elif x == 0:
    print(0)
elif x == 1:
    print(fib1)
elif x == 2:
    print(fib1, fib2)
else:
    x = int(x) - 2
    print(fib1, fib2, end=' ')

    while x > 0:
        fib1, fib2 = fib2, fib1 + fib2
        x -= 1
        print(fib2, end=' ')
