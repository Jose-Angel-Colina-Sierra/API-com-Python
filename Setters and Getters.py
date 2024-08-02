# class Persona:
#     def __init__(self,nombre,edad):
#         self.__nombre = nombre
#         self.__edad = edad

#     def get_edad_nombre(self , new_nombre):

#         self.__nombre = new_nombre
#         return self.__edad , self.__nombre
        
    
# jose = Persona("Jose", 21)

# edad_nombre = jose.get_edad_nombre('daniel')

# print(edad_nombre[0])
# print(edad_nombre[1])

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        return self.__nombre
    
jose = Persona('Jose',23)

nombre = jose.get_nombre()

print(nombre)

change_name = jose.set_nombre('Fernando')
nombre = change_name

print(nombre)
print(jose.__edad)