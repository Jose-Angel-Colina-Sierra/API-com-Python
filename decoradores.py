def mamita(funcion):
    def funcion_modificada():
        print('Antes de ejecutar la funcion')
        funcion()
        print('Despues de ejecutar la funcion')
    return funcion_modificada

# def saludo():
#     print('Hola Jose, como andas?')


# saludo_modificado = decorador(saludo)

# saludo_modificado()

@mamita
def saludo():
    print('Hola Jose, como andas?')

saludo()