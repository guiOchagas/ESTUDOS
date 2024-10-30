"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""

class Bola():
    def __init__ (self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self. material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'{self.cor}')

bola1 = Bola('Vermelho', 20, 'Plástico')

print(bola1.cor, bola1.circunferência, bola1.material)

bola1.trocaCor('Azul')
bola1.trocaCor('Rosa')


bola1.mostraCor()
