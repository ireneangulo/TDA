listanombre= []
listalargo= []
listatripulacion= []
listacantidadpasajeros= []
listageneral= []
class Starwars:
    def __init__(self,nombre, largo, tripulacion,cantidadpasajeros):
        self.nombre= nombre
        self.largo= largo
        self.tripulacion= tripulacion
        self.cantidadpasajeros= cantidadpasajeros
    
       

Halconmilenario = Starwars ("Halconmilenario", 24865, 6, 873)
Estrelladelamuerte = Starwars("Estrella de la muerte",50765, 4, 4700)
Machupichu = Starwars("Machupichu",17849, 5, 2876)
Lamuerte = Starwars("La muerte",4566, 3, 743)
Atrapado = Starwars("Atrapado",7654, 5, 973)
Calavera = Starwars("Calavera",5078, 7, 470)
listacantidadpasajeros.append(Halconmilenario.cantidadpasajeros)
listacantidadpasajeros.append(Estrelladelamuerte.cantidadpasajeros)
listacantidadpasajeros.append(Machupichu.cantidadpasajeros)
listacantidadpasajeros.append(Lamuerte.cantidadpasajeros)
listacantidadpasajeros.append(Atrapado.cantidadpasajeros)
listacantidadpasajeros.append(Calavera.cantidadpasajeros)
listatripulacion.append(Halconmilenario.tripulacion)
listatripulacion.append(Estrelladelamuerte.tripulacion)
listatripulacion.append(Machupichu.tripulacion)
listatripulacion.append(Lamuerte.tripulacion)
listatripulacion.append(Atrapado.tripulacion)
listatripulacion.append(Calavera.tripulacion)
listalargo.append(Halconmilenario.largo)
listalargo.append(Estrelladelamuerte.largo)
listalargo.append(Machupichu.largo)
listalargo.append(Lamuerte.largo)
listalargo.append(Atrapado.largo)
listalargo.append(Calavera.largo)
listageneral.append(Halconmilenario)
listageneral.append(Estrelladelamuerte)
listageneral.append(Machupichu)
listageneral.append(Lamuerte)
listageneral.append(Atrapado)
listageneral.append(Calavera)

# APARTADO 1
print("\nMostrando información Halcon Milenario:")
print("\nLongitud: ",Halconmilenario.largo)
print("\nTripulación: ",Halconmilenario.tripulacion)
print("\ncantidadpasajeros: ",Halconmilenario.cantidadpasajeros)

print("\nMostrando información Estrella de la muerte:")
print("\nLongitud: ",Estrelladelamuerte.largo)
print("\nTripulación: ",Estrelladelamuerte.tripulacion)
print("\nCantidad de pasajeros: ",Estrelladelamuerte.cantidadpasajeros)

#APARTADO 2
listacantidadpasajeros.sort(reverse= True)
print(listacantidadpasajeros)
for i in range (5):
    print(listacantidadpasajeros[i])
print("Como podemos observar las naves con mayor cantidad de pasajeros son, Estrella de la muerte, Machupichu, Atrapado, Halconmilenario y La muerte")

#APARTADO 3
listatripulacion.sort(reverse= True)
print(listatripulacion[0])  
print("La nave con mayor tripulación es Calavera")
# APARTADO 4
#for i in listageneral:
#   if i.nombre[0]=="A" & i.nombre[1]== "t":
#       print[i]

#APARTADO 5

listalargo.sort(reverse=True)
print("\n La nave con longitud más grande es La muerte con una longitud de :",listalargo[0])

print("\n La nave con longitud más grande es la Estrella de la muerte con una longitud de :",listalargo[-1])
