class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f"""Datos:
            Nombre: {self.nombre}
            Edad: {self.edad}"""
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        return f"""El grado del estudiante es: {self.grado}"""

estudiante_1 = Estudiante("Jose",21,"Quinto Grado")  

print(estudiante_1.mostrar_datos())
print(estudiante_1.mostrar_grado())


