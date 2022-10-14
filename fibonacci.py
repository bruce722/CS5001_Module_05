from functools import reduce


def fibonacci(n):
    return reduce(lambda a, _: a+[a[-1]+a[-2]], range(n-2), [1, 1])


if __name__ == '__main__':
    print(fibonacci(10))
