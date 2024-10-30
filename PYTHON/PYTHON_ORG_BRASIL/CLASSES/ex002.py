"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado():
    def __init__ (self, lado):
        self.lado = lado
    
    def mudarValor(self, lado):
        self.lado = lado
    
    def retornarValor(self):
        print(f'O valor do quadrado é {self.lado}')
    
    def calcularArea(self):
        area = self.lado * self.lado
        print(f'O valor dos lados do quadrado é {self.lado} e o cálculo da área é {area}')


square = Quadrado(10)

square.mudarValor(50)

square.retornarValor()

square.calcularArea()
