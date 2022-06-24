num = int(input("Escribir un numero: "))
num2 = int(input("Escribir un divisor: "))
c = 0
if num%2 == 0:
    print("El numero es par")
    c = 1
if num%4 == 0:
    print("El numero es divisible por 4")
    c = 1
if num%num2 == 0:
    print("El numero es divisible por " + str(num2))
    c = 1
if c == 0:
    print("El numero no es divisible por 2 ni 4 ni " + str(num2))