#Creación de la matriz
def crear_matriz(numero_filas, numero_columnas):
    matriz= [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None]*numero_columnas
    return matriz
    

#He creado el determinante de una matriz por el metodo de Sarrus
def determinante_grado_3(m3):
    A1= m3[0][0]*m3[1][1]*m3[2][2]+ m3[1][0]*m3[2][1]*m3[0][2]+m3[2][0]*m3[1][2]*m3[0][1]
    A2= m3[0][2]*m3[1][1]*m3[2][0]+ m3[1][2]*m3[2][1]*m3[0][0]+m3[0][1]*m3[1][0]*m3[2][2]
    return A1 - A2

def dibujar_matriz(m3):
    print("La matriz es: ")
    for i in range(len(m3)):
        print(m3[i])

matriz= [[3,6,4],[7,1,8],[9,5,2]]
dibujar_matriz(matriz)
print("El determinante según el método de Sarrus es: ",determinante_grado_3(matriz))