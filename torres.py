def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"mover el disco 1 de {origen} a {destino}")
        return
    hanoi(n-1, origen, auxiliar, destino)
    print(f"mover el disco {n} de {origen} a { destino}")
    hanoi(n-1, auxiliar, destino , origen)

num = int(input("ingrese el numero de discos: "))
hanoi(num, 'A','C','B')
