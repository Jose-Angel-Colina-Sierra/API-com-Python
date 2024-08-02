#Os properties permitem gerar getters, setters and deletters 
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre


jose = Persona('Jose',23)

nombre = jose.nombre
print(nombre)

jose.nombre = "daniel"

nombre = jose.nombre
print(nombre)

del jose.nombre
