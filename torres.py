def hanoi(n, origen, destino, auxiliar):
    global pasos

    if n == 1:
        print(f"paso {pasos}: mover el disco 1 de {origen} a {destino}")
        pasos += 1
        return
    
    hanoi(n-1, origen, auxiliar, destino)
    print(f"paso {pasos}: mover el disco {n} de {origen} a { destino}")
    pasos += 1
    hanoi(n-1, auxiliar, destino , origen)

pasos = 1
num = int(input("ingrese el numero de discos: "))
hanoi(num, 'A','C','B')
print(f"el numero de pasos: {pasos - 1}" )