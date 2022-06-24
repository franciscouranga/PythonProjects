palabra = str(input("0: ")).upper()
n = int(input("1: "))
c = 0
prueba1 = palabra.lower()
conta = 0

while True:
    while True:
        x = str(input("2: ")).upper()
        if len(x) == 1: break
    if x in palabra:
        prueba = ""
        for s in prueba1:
            if x == s.upper():
                prueba = prueba + x
            else:
                prueba = prueba + s
        prueba1 = prueba
    else:
        c += 1
    conta += 1
    if c > n:
        print(0)
        break
    elif prueba == palabra:
        print(conta)
        break
