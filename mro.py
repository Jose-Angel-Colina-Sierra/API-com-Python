class A:
    def hablar(self):
        print("Hola desde F")

class F:
    pass

class B(A):
    pass

class C(F):
    pass
    

class D(B,C):
    pass


d = D()

d.hablar()