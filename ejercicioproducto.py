class Producto:
    '''Clase Producto'''
    
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("Producto {} creado".format( self.codigo))
                
# Experimentacion
p1 = Producto(1, "Rolex", 1000, "Relojeria")
p2 = Producto(2, "Zadig&Voltaire", 470, "Moda")
p3 = Producto(3, "Tesla", 200000, "Vehículo")

print("\nMostrando información:")
print(p1.codigo)
print(p1.nombre)
print(p1.precio)
print(p1.tipo)

print("\nModificando información:")
print("Cambiando precio al producto 3")
print("Antes:", p3.precio)
p3.precio = 150000
print("Despues:", p3.precio)