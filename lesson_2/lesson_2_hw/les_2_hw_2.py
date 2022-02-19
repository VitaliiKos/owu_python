"""
написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
- первый записывает в эту переменную запись
- второй возвращает все записи

запишите 5 тудушек
и выведете все
"""


def notebook() -> []:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list:
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()
add_todo('Max')
add_todo('Masha')
add_todo('Misha')
add_todo('Melvin')
add_todo('Mario')
add_todo('Madrid')
add_todo('Mephistopheles')
print(get_all())
