name = input("Nombre: ")
age = int(input("Edad: "))
cumple = 100 - age + 2020
number = int(input("Cuantas veces imprimo esto: "))
for i in range(number):
    print("\nHola " + name + ", vas a cumplir 100 años en " + str(cumple))