# class MiClase:
#     def __init__(self):
#         self.__atributo_privado = "valor"

# objeto = MiClase()

# print(objeto.__atributo_privado)


# class MiClase:
#     def __init__(self):
#         self.__atributo_privado = "valor"
    
#     def obtener_atributo_privado(self):
#         return self.__atributo_privado
    
#     def establecer_atributo_privado(self, valor):
#         self.__atributo_privado = valor

# objeto = MiClase()

# # Acessando o atributo privado através de um método público
# print(objeto.obtener_atributo_privado())


class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"
    
    def _comer(self):
        return 'Estoy Comiendo'

objeto = MiClase()

print(objeto._comer())

