class Alumno:
    __dni=0
    __nombre=""
    __apellido=""
    __carrera=""
    __año=0
    
    
    def __init__ (self,dni,apellido,nombre,carrera,año):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__carrera=carrera
        self.__año=año
        
        
    def getAño(self):
        return self.__año
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def mostrar (self):
        print("dni {}, nombre {}, apellido {}, carreras {}, año {}".format(self.__dni,self.__nombre,self.__apellido,self.__carrera,self.__año))
        
        
    def __gt__(self,otroAlumno):
        primero=str(self.__año)+str(self.__apellido)
        segundo=str(otroAlumno.__año)+str(otroAlumno.__apellido)
        return (primero>segundo)