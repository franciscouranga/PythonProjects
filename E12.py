# TRANSFORMA LISTAS EN SOLO VALOR INICIAL Y FINAL

def trim_lists(list):
    if len(list) < 2:
        print("List is invalid.")
        exit()
    lista = []
    lista.append(list[0])
    lista.append(list[-1])
    return lista


if __name__ == "__main__":
    lis = [1, 3, 5, "a"]
    print(trim_lists(lis))
