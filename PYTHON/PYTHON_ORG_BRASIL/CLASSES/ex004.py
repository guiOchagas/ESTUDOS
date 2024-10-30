"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""


class Pessoa():
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def Envelhecer(self):
        self.idade += 1
        
    def Engordar(self):
        self.peso += 5
        
    def Emagrecer(self):
        self.peso -= 1
        
    def Crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.Envelhecer()
    

person = Pessoa('Gui', 20, 83, 184)

person.Crescer()

print(person.nome, person.idade, person.peso, person.altura)

