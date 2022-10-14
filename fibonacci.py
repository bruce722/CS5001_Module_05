from functools import reduce


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    return reduce(lambda a, _: a + [a[-1] + a[-2]], range(n-2), [1, 1])


if __name__ == '__main__':
    print(fibonacci(2))
