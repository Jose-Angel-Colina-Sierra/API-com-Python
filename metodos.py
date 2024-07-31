class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print(f"Estas llamando desde un {self.marca} de modelo: {self.modelo}")
    def cortar(self):
        print(f"Cortaste la llamada desde un {self.marca} de modelo: {self.modelo}")
    
    
celular_1 = Celular("samsung","S23","48MP")
celular_2 = Celular("Apple","Iphone 15","48MP")

celular_1.llamar()