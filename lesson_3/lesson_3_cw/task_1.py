"""
Создать класс Rectangle:
-конструктор принимает две стороны x,y
-описать арифметические методы:
  + сума площадей двух экземпляров класса
  - разница площадей
  == или площади равны
  != не равны
  >, < меньше или больше
  при вызове метода len() подсчитывать сумму сторон
"""


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'{((self.x + self.y) * 2)} + {((other.x + other.y) * 2)} = ' \
               f'{((self.x + self.y) * 2) + ((other.x + other.y) * 2)}'

    def __sub__(self, other):
        return f'{((self.x + self.y) * 2)} - {((other.x + other.y) * 2)} = ' \
               f'{((self.x + self.y) * 2) - ((other.x + other.y) * 2)}'

    def __eq__(self, other):
        return f'{((self.x + self.y) * 2)} == {((other.x + other.y) * 2)} -> ' \
               f'{((self.x + self.y) * 2) == ((other.x + other.y) * 2)}'

    def __ne__(self, other):
        return f'{((self.x + self.y) * 2)} != {((other.x + other.y) * 2)} -> ' \
               f'{((self.x + self.y) * 2) != ((other.x + other.y) * 2)}'

    def __gt__(self, other):
        return f'{((self.x + self.y) * 2)} > {((other.x + other.y) * 2)} -> ' \
               f'{((self.x + self.y) * 2) > ((other.x + other.y) * 2)}'

    def __lt__(self, other):
        return f'{((self.x + self.y) * 2)} < {((other.x + other.y) * 2)} -> ' \
               f'{((self.x + self.y) * 2) < ((other.x + other.y) * 2)}'

    def __len__(self):
        return (self.x + self.y) * 2


rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)

print((rectangle1 + rectangle2))
print((rectangle1 - rectangle2))
print((rectangle1 == rectangle2))
print((rectangle1 != rectangle2))
print((rectangle1 > rectangle2))
print((rectangle1 < rectangle2))
print(len(rectangle1))
