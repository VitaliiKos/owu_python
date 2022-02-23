""""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name,
та який наслідуются від класу Printable
3) Створити свій кастомний Exception
4) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

4)всі методи класу Main запускати в try except, приклад:
try:
    Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazineі()
    print('-' * 40)
    Main.show_all_bookі()
except NonBookMagazineException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)
"""
from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, book_name):
        self.book = book_name

    def print(self):
        print(self.book)


class Magazine(Printable):

    def __init__(self, magazine_name):
        self.magazine = magazine_name

    def print(self):
        print(self.magazine)


class NonBookMagazineException(Exception):
    pass


class Main:
    printable_list = []

    @classmethod
    def add(cls, new_book):
        """
        метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
         чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
        :return:
        """
        if not isinstance(new_book, (Book, Magazine)):
            raise NonBookMagazineException

        cls.printable_list.append(new_book)

    @classmethod
    def show_all_magazines(cls):
        """
        метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
        :return:
        """
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        """
        метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
        :return:
        """

        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


if __name__ == '__main__':
    try:
        Main.add(Magazine('Magazine1'))
        Main.add(Book('Book1'))
        Main.add(Magazine('Magazine3'))
        Main.add(Magazine('Magazine2'))
        Main.add(Book('Book2'))
        Main.show_all_magazines()

        print('-' * 40)
        Main.show_all_books()
        Main.add(333)
    except NonBookMagazineException:
        print('Це не журнал або книжка')
    except Exception as err:
        print(err)
