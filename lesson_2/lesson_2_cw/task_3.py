import time


def my_decor(func):
    sum_time = 0

    def wraper():
        nonlocal sum_time

        start = time.time()
        func()
        sum_time += time.time() - start
        print('Total execution time', sum_time)
    return wraper


@my_decor
def func_1():
    l = [i for i in range(50000000)]


func_1()
func_1()
func_1()
