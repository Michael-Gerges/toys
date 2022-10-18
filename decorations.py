# this is actually a useful example - decorator is used to measure
# time taken to execute a function


def timeit(func, *args, **kwargs) :
    def inner(*args, **kwargs) :
        import time
        start = time.time()
        retval = func(*args, **kwargs)
        finish = time.time() - start
        return finish, retval

    return inner


@timeit
def adder(a) :
    return sum(a)


adder = timeit(adder)

print(adder(range(10)))
