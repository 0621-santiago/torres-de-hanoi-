def hanoi(n, origen, destino, auxiliar):
    global pasos
    #definimos la funcion de las torres y lo que no añadira los pasos 
    
    if n == 1:
        print(f"paso {pasos}: mover el disco 1 de {origen} a {destino}")
        pasos += 1
        return
    #es la encargada de hacer el movimiento para que en el siguiente bloque nos permita aumentar el numero de movimientos 

    hanoi(n-1, origen, auxiliar, destino)
    print(f"paso {pasos}: mover el disco {n} de {origen} a { destino}")
    pasos += 1
    hanoi(n-1, auxiliar, destino , origen)
    #es la parte que se encargar de mover los discos de una torre a otra 

while True:
    try:
        num = int(input("ingrese el numero de discos:" ))
    except ValueError:
        print("ingrese un numero, no una letra, gracias")
    else:
        break

pasos = 1
hanoi(num, 'A','C','B')
print(f"el numero de pasos es: {pasos - 1}" )