class funcionario():
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def dados(self):
        return {'nome': self.nome , 'salario': self.salario}
    

fabio = funcionario("Jose", 7000)

print(fabio.dados())


class admin(funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self,nome):
        self.nome = nome
        return self.dados()
    
fernando = admin("daniel", 9000)
print(fabio.dados())
print(fernando.atualizar_dados('Daniel'))

