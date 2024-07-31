#1 EJERCICIO //////////////////////////////////


class estudiante:
    def __init__(self,Nombre,Edad,Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado
        
    def estudiar(self):
        print("Estudiando...")

Nombre = input("Digita seu Nome: ")
Edad = input("Digita sua Idade: ")
Grado = input("Digita seu Grado: ")

Estudiante = estudiante(Nombre,Edad,Grado)


print(f"""
    Datos del estudiante: \n
    Nombre: {Estudiante.Nombre} \n
    Edad: {Estudiante.Edad} \n
    Grado: {Estudiante.Grado} \n
    """)


while True:
    estatus_estudio = input()

    if (estatus_estudio.lower() == "estudiar"):
        Estudiante.estudiar()

#2 EJERCICIO //////////////////////////////////

class vehiculo:

    def __init__(self,Marca,Modelo,Ano):
        
        self.marca = Marca
        self.modelo = Modelo
        self.ano = Ano\
        
    def conducir(self):
        print("Conduciendo...")

marca = input("digita a marca do seu carro: ")
modelo = input("digita o modelo do seu carro: ")
ano = input("digita o ano do seu carro: ")

carro_cliente = vehiculo(marca,modelo,ano)


while True:
    comando = input("Escribe 'conducir' para conducir el vehículo: ")
    if (comando.lower() == "conducir"):
        carro_cliente.conducir()
        break

#3 EJERCICIO //////////////////////////////////

class Livro:
    def __init__(self,titulo,autor,paginas):
        
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def leer(self):
        print("Leyendo...")

titulo = input("Digita o titulo do seu livro aqui: ")
autor = input("Digita o Autor do seu livro aqui: ")
Paginas = input("Digita quantas paginas tem seu livro aqui: ")

livro = Livro(titulo,autor,Paginas)

print(f"""
        Os dados do livro sao: \n
        Titulo do livro: {livro.titulo} \n
        Autor do livro: {livro.autor} \n
        Quantas paginas tem o livro: {livro.paginas} \n
""")


while True:
    comando = input("Digita o comando 'leer' para leer o livro: ")
    if (comando.lower() == "leer"):
        livro.leer()
        break