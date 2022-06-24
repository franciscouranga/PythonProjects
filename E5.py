lista1 = [1, 3, 5, 7, 9]
lista2 = [1, 2, 3, 7]


'''OPCION 1 LISTAS
lista3 = []

for i in lista1:
    for j in lista2:
        if i == j:
            lista3.append(i)
print(lista3)
'''


# opcion 2 de una linea
# print([a for a in lista1 for b in lista2 if a == b])

#OPCION 3 CON SETS

print(list(set(lista1).intersection(lista2)))