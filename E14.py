'''
OPCION 1 USANDO SETS

names = set()
names.add("nico")
names.add("nico")
print(list(names)) #esto lo hago para imprimir en forma de lista y no como set

'''

# Opcion 2 usando listas

lista = []
while True:
    m = input("Agregar a lista: (exit) ")
    if m == "exit":
        break
    else:
        lista.append(m)
lista_final = []
for item in lista:
    if item not in lista_final:
        lista_final.append(item)
print(lista_final)
