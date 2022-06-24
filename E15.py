#CAMBIAR EL ORDEN DE LAS PALABRAS EN UNA FRASE
import string

def cambiar_orden_palabras(frase):
    lis = frase.split()
    dev = ''
    c = 1
    while c <= len(lis):
        dev = dev + lis[-c] + " "
        c += 1
    return dev


if __name__ == "__main__":
    fras = str(input("Escribir una frase: "))
    print(cambiar_orden_palabras(fras))
    print(fras.split())
