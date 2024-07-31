class funcionario:

    aumento = 1.04
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome , 'salario': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    # @classmethod
    # def definir_novo_aumento(cls):
    #     cls.aumento = novo_aumento


fabio = funcionario('fabio', 1000)

fabio.aplicar_aumento()
print(fabio.dados())