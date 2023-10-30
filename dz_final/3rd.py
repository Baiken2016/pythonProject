def fib_decorator(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)

        return cache[n]

    return wrapper


@fib_decorator
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))