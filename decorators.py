import random
import time
import functools


def debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        time_delta = time_end - time_start
        print(f'[{func.__name__}] {time_delta} seconds')
        print(f'arguments: {tuple(arg for arg in args)}')
        print(f'keyword arguments: {kwargs}')
        print(f'result: {result}')
        print()
        return result

    return wrapper


@debugger
def sort_large_amount_of_data():
    numbers = [random.randint(0, 1000000) for _ in range(1000000)]
    numbers.sort()


@debugger
def stdev(*args):
    n = len(args)
    mean = sum(args) / n
    variance = sum((x - mean) ** 2 for x in args) / (n - 1)
    return variance ** 0.5


if __name__ == '__main__':
    stdev(1, 2, 3, 4, 5)
