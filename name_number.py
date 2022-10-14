from functools import reduce


def name_number(name):
    return reduce(lambda a, b: a + ord(b.lower()) - 96, list(name), 0)


if __name__ == '__main__':
    print(name_number("Jump"))
