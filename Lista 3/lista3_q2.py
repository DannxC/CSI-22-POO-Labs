# EXEMPLO 1
class A:
    def who_am_i(self):
        return "A"

class B(A):
    def who_am_i(self):
        return "B"

class C(A):
    def who_am_i(self):
        return "C"

class D(B, C):
    pass

obj = D()
print(obj.who_am_i())  # Imprime "B"
print(D.mro())  # Imprime a ordem de resolução de métodos

# EXEMPLO 2
class E:
    def who_am_i(self):
        return "E"

class F:
    def who_am_i(self):
        return "F"

class G(E, F):
    def who_am_i(self):
        return "G"

class H(E):
    pass

class I(F):
    def who_am_i(self):
        return "I"

class J(G, H, I):
    pass

obj2 = J()
print(obj2.who_am_i()) # Imprime "G"
print(J.mro()) # Imprime a ordem de resolução de métodos
