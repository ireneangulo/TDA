matriz = []


#Funciones
def mat(n):
    for i in range (n):
        matriz.append([])
        for j in range (n):
            matriz[i].append(0)
    return matriz

def llenar(n):
    matriz = mat(n)
    for x in range (n):
        for y in range (n):
            matriz[x][y] = float(input('Valor de [' + str(x) + '][' + str(y) + '] = '))

    #He creado el determinante de una matriz por el metodo de Sarrus
    def determinante_grado_3(n):
        A1= n[0][0]*n[1][1]*n[2][2]+ n[1][0]*n[2][1]*n[0][2]+n[2][0]*n[1][2]*n[0][1]
        A2= n[0][2]*n[1][1]*n[2][0]+ n[1][2]*n[2][1]*n[0][0]+n[0][1]*n[1][0]*n[2][2]
        return A1 - A2

    def im(n):
        print("\nMatriz resultante:")
        for i in range (n):
                print (matriz[i][:])

#Programa

    n = int(input ('Tamano de la matriz : '))
    llenar(n)
    im(n)
    determinante_grado_3(n)
    input()