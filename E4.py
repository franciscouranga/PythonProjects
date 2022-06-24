def buscar_divisores():

    while True:
        try:
            num = int(input("Ingresa numero para buscar los divisores: "))
            break
        except ValueError:
            print("Not valid")
    numeros = []
    for i in range(1, num + 1):
        if num % i == 0:
            numeros.append(i)
    return numeros


if __name__ == "__main__":

    print(buscar_divisores())
