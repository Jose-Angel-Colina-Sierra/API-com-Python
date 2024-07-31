class Jogador_loteria:
    def __init__(self,nome):
        self.nome = nome
        self.numeros = [13,4,52,23,67,82]
    
    def total(self):
        return sum(self.numeros)
    
jogador_1 = Jogador_loteria("Jose")
jogador_2 = Jogador_loteria("Maria")

print(jogador_1.nome)
print(jogador_2.nome)

print(jogador_1.total())
print(jogador_2.total())

print(jogador_1 == jogador_2)