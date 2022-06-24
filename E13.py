def fibonacci(n):

    a = i = a1 = 0
    b = 1
    list = [b]
    while i < n - 1:
        a1 = b
        b = a + b
        a = a1
        list.append(b)
        i += 1
    return list


if __name__ == "__main__":
    m = int(input("Cuantos Fibonacci queres hacer: "))
    print(fibonacci(m))