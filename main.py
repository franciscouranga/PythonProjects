array = [1, 2, 3, 4, 7, 9, 21]
sequence = [1, 3, 7, 21]
numero_ant = -1
exit_list = False

for number in sequence:
    if number not in array:
        exit_list = True
        print("No es un sub")
        exit()
    numero1 = array.index(number)
    if numero_ant >= numero1:
        print("No es un sub")
        exit_list = True
    numero_ant = numero1

if exit_list == False:
    print("Es un sub")
