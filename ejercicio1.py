def torrehanoi(discos):
    if discos == 1:
        contador = 1
    else:
        contador = (2 * torrehanoi(discos-1) + 1)
    return contador

def movimientos():
    discos = int(input("Introduzca el número total de discos de la Torre de Hanói:"))
    print("{} los discos deben moverse: {} veces".format(discos, torrehanoi(discos)))

movimientos()