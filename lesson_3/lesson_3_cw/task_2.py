"""
создать класс Human (name, age)
создать два класса Prince и Cinderella:
у золушки должно быть имя возраст и размер ноги
у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет
ту самую

класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
и метод класса который будет показывать это количество
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
        Cinderella.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        return f'Власницею туфельки виявилась {self.name}. Їй {self.age} роки!'


class Prince(Human):
    def __init__(self, name, age, shoe):
        super().__init__(name, age)
        self.shoe = shoe

    def find_cinderella(self, girls: list[Cinderella]):
        for girl in girls:
            if girl.size == self.shoe:
                return girl


girls = [
    Cinderella('Kira', 22, 34),
    Cinderella('Karina', 223, 33),
    Cinderella('Ksenia', 24, 32),
    Cinderella('Katia', 32, 36),
    Cinderella('Katerina', 33, 38),
]
prince = Prince('Valdemar', 22, 32)

print(prince.find_cinderella(girls))
