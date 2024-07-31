#Herencia Simple ///////////////////////////////////////////////////

# class Persona:
#     def __init__(self,nombre,edad,nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
#     def hablar(self):
#         print(f"Hola, estoy hablando con {self.nombre}")
# class Empleado(Persona):
#     def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
#         super().__init__(nombre,edad,nacionalidad)
#         self.trabajo = trabajo
#         self.salario = salario

#Herencia jerarquica \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Persona:
#     def __init__(self,nombre,edad,nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
#     def hablar(self):
#         print(f"Hola, estoy hablando con {self.nombre}")
# class Empleado(Persona):
#     def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
#         super().__init__(nombre,edad,nacionalidad)
#         self.trabajo = trabajo
#         self.salario = salario

# class Estudiante(Persona):
#     def __init__(self,nombre,edad,nacionalidad,carrera,id_estudiante):
#         super().__init__(nombre,edad,nacionalidad)
#         self.carrera = carrera
#         self.id_estudiante = id_estudiante

# daniel = Persona("Daniel",19,"argentino")
# Mario = Empleado("Mario",42,"argentino","Programador",3000)
# roberto = Estudiante("Roberto",28,"argentino","Analisis de sistemas","A123GH")

# roberto.hablar()

# print(f"""
#     Datos de la persona: \n
#     Nombre: {daniel.nombre} \n
#     Edad: {daniel.edad} \n
#     Nacionalidad: {daniel.nacionalidad} \n
# """)

# print(f"""
#     Datos del empleado: \n
#     Nombre: {Mario.nombre} \n
#     Edad: {Mario.edad} \n
#     Nacionalidad: {Mario.nacionalidad} \n
#     Carrera: {Mario.trabajo} \n
#     Salario: {Mario.salario} \n
#     """)

# print(f"""
#     Datos del estudiante: \n
#     Nombre: {roberto.nombre} \n
#     Edad: {roberto.edad} \n
#     Nacionalidad: {roberto.nacionalidad} \n
#     Carrera: {roberto.carrera} \n
#     id de estudiante: {roberto.id_estudiante} \n
#     """)


#Herencia Multiple \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Persona:
#     def __init__(self,nombre,edad,nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
#     def hablar(self):
#         print(f"Hola, estoy hablando con {self.nombre}")

# class Artista:
#     def __init__(self,habilidad):
#         self.habilidad = habilidad

#     def mostrar_habilidad(self):
#         return f"Mi habilidad es {self.habilidad}"

# class EmpleadoArtista(Persona,Artista):
#     def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
#         Persona.__init__(self,nombre,edad,nacionalidad)
#         Artista.__init__(self,habilidad)

#         self.salario = salario
#         self.empresa = empresa

#     def presentarse(self):
#         return f"Hola me llamo {self.nombre}, soy de {self.nacionalidad} y tengo {self.edad} anos de edad, {super().mostrar_habilidad()} \n y trabajo en {self.empresa}"
    


# Daniel = EmpleadoArtista("Mario",42,"argentino","Bailar",3000,"Google")

# print(Daniel.presentarse())


# herencia = issubclass(EmpleadoArtista,Persona)
# instancia = isinstance(Daniel,Artista)
# print(instancia)






