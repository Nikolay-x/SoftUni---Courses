def create_sequence(n):
    result = []
    if n == 1:
        result.append(0)
    elif n == 2:
        result.append(0)
        result.append(1)
    elif n > 2:
        result.append(0)
        result.append(1)
        for i in range(3, n+1):
            result.append(result[-1] + result[-2])

    return result


def locate(x, line):
    if x not in line:
        print(f"The number {x} is not in the sequence")
    else:
        index = line.index(x)
        print(f"The number - {x} is at index {index}")



