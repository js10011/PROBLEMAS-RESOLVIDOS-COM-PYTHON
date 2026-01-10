
'''Crie duas classes básicas Base1 e Base2, cada uma com um método describe().
Crie uma classe derivada Combined, que herda de ambas as classes básicas.
Implemente o método describe() em cada classe básica. Chame o método describe() no objeto da classe Combined.'''
class Base1:
    def describe(self):
        print("Essa eh a Base1")

class Base2:
    def describe(self):
        print("Esta eh a  Base2")

class Combined(Base1, Base2):
    pass

obj = Combined()
obj.describe()

'''Crie duas classes base BaseA e BaseB, cada uma com um método action().
Crie uma classe derivada Derived com um método action() sobrescrito, que chama o método super().action().
Chame o método action() em um objeto da classe Derived e analise a ordem dos chamados dos métodos'''

class BaseA:
    def action(self):
        print("Acao da  BaseA")
        
class BaseB:
    def action(self):
        print("Acao da BaseB")

class Derived(BaseA, BaseB):
    def action(self):
        super().action()
        print("Action from Derived")

d = Derived()
d.action()

'''Crie as classes A, B, C e D, onde B e C herdam de A, e D herda de B e C.
Em cada classe, defina o método method que imprime o nome da classe e chama o método super().method().
Crie uma instância da classe D e chame o método method para entender a ordem de chamada dos métodos segundo o MRO.'''
class A:
    def method(self):
        print("A")
        # Sem chamada para super() porque A é a classe mais alta na hierarquia

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

d = D()
d.method()

'''Crie as classes M, N e O, onde N e O herdam de M.
Em cada classe, defina o método action, que imprime o nome da classe
e chama o método da classe pai usando super().
Verifique a ordem de chamada dos métodos, criando uma instância da classe N e chamando o método action.'''
class M:
    def action(self):
        print("Class M action")

class N(M):
    def action(self):
        print("Class N action")
        super().action()

class O(M):
    def action(self):
        print("Class O action")
        super().action()

n = N()
n.action()