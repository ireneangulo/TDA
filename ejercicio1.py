def hanio(discos):
    if discos == 1:
        contador = 1
    else:
        contador = (2 * hanio(discos-1) + 1)
    return contador

def movimientos():
    discos = eval(input("Introduzca el número total de discos de la Torre de Hanói:"))
    print("{} los discos deben moverse: {} veces".format(discos, hanio(discos)))

movimientos()