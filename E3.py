
n = int(input("Largo de la lista: "))
lista = []
i = 0
lista_imprimir = []
while i < n:
    lista.append(float(input("Numero " + str(i+1) + ": ")))
    if lista[i] <= 5:
        lista_imprimir.append(lista[i])
    i += 1

for menores in lista_imprimir:
    print(menores)

# Opcion 2
# print([aa for aa in [1, 3, 6, 8] if aa < 5])

#Opcion 3
''' 
a = [1, 3, 4, 7, 9]
for num in a:
    if num < 5:
        print(num)
'''