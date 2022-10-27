class Alumno:
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con exito")
 
    def calificacion(self):
        if self.nota < 5:
            print("El alumno {} ha suspendido".format(self.nombre))
        else:
            print("El alumno {} ha aprobado".format(self.nombre))
 
 # Creacion de alumnos
alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Alfredo", 3)
 
# Comprobamos
alumno1.calificacion()
alumno2.calificacion()

# SEGUNDA PARTE EJERCICIO
class Alumno:
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con exito")
 
    def __str__(self):
        return "Nombre: {}\n\tNota: {}".format(self.nombre, self.nota)
 
    def calificacion(self):
        if self.nota < 5:
            print("El alumno {} ha suspendido".format(self.nombre))
        else:
            print("El alumno {} ha aprobado".format(self.nombre))
 
 # Creacion de alumnos
alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Alfredo", 3)
 
# Comprobamos
print(alumno1)
print(alumno2)