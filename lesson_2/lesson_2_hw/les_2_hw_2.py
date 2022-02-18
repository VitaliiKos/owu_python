"""
написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
- первый записывает в эту переменную запись
- второй возвращает все записи

запишите 5 тудушек
и выведете все
"""
from typing import Callable


def notebook() -> Callable:
    todo_list = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list:
        return todo_list

    def func() -> None:
        pass

    func.add_todo = add_todo
    func.get_all = get_all

    return func


todo_func = notebook()
todo_func.add_todo('Max')
todo_func.add_todo('Masha')
todo_func.add_todo('Misha')
todo_func.add_todo('Melvin')
todo_func.add_todo('Mario')
todo_func.add_todo('Madrid')
todo_func.add_todo('Mephistopheles')
print(todo_func.get_all())
