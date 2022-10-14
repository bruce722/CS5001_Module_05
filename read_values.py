

def read_values():
    result = []
    num = int(input("Enter a number: "))
    while num > 0:
        result.append(num)
        num = int(input("Enter a number: "))
    return result


if __name__ == '__main__':
    print(read_values())
