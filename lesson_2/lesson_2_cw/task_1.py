def my_decortion(a_func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1

        print(a_func.__name__, count)

        a_func()

        print('---------------------------')

    return wrapper


@my_decortion
def func_1():
    print("func_1")


@my_decortion
def func_2():
    print("func_2")


func_1()
func_1()
func_1()
func_2()
func_1()
