class Animal:
    def comer(self):
        print("El animal esta comiendo")
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantanto")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        

class Murcielago(Mamifero,Ave):
    def amamantar(self):
        print("El animal esta amamantanto pero como murcielago")
        super().amamantar()


murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())