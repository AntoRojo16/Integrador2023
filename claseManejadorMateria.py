import csv
from claseMateriasAprobadas import Materia


class MateriasAprobadas:
    __materias = []

    def __init__(self):
        self.__materias = []

    def agregarMateria(self, unaMateria):
        self.__materias.append(unaMateria)

    def inicializar(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dni = fila[0]
                nombre = fila[1]
                fecha = fila[2]
                nota = fila[3]
                aprobacion = fila[4]
                unaMateria = Materia(dni, nombre, fecha, nota, aprobacion)
                self.agregarMateria(unaMateria)
        archivo.close()

    def __str__(self):
        
        s = ""
        for materia in self.__materias:
            s += str(materia) +"\n"

        return s
    
    def calcularMaterias(self):
        dni=input('Ingrese el dni')
        cont=0
        suma=0
        for materia in self.__materias:
            if materia.getDni()==dni:
                cont+=1
                suma+=int(materia.getNota())

        print("Su promedio es: {}".format((suma/cont)))



    def ejercicio2 (self,alumnos):
        nombre=input("Ingrese el nombre de la materia")

        for materia in self.__materias:
            if materia.getNombre==nombre:
                if (materia.getNota()>=7):
                    alumnos.buscarDni(materia.getDni())
                    
        