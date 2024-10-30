"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local."""


class Retangulo():
    def __init__ (self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        
    def mudarValor(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mostrarValor(self):
        print(f'Comprimento: {self.ladoA}\nLargura: {self.ladoB}')
    
    def calcularArea(self):
        area = self.ladoA * self.ladoB
        print(f'A área é: {area}')
    
    def calcularPerimetro(self):
        perimetro = (self.ladoA * 2) + (self.ladoB * 2)
        print(f'O perímetro é: {perimetro}')
    

comprimento = int(input('Informe o comprimento: '))
largura = int(input('Informe a largura: '))

result = Retangulo(comprimento, largura)

result.calcularArea()

result.calcularPerimetro()



