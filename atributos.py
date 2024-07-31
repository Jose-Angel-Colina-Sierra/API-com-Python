#son variables que pertenecen a una clase

class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    
celular_1 = Celular("samsung","S23","48MP")
celular_2 = Celular("Apple","Iphone 15","48MP")
celular_3 = Celular("Huawei","P20 Pro","148MP")


print(celular_1.marca)
print(celular_2.marca)
print(celular_3.marca)

