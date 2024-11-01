"""Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem."""


"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""


from random import randint


class Poe():
    
    def __init__(self, nome, fome=None, saude=100):
        self.nome = nome
        self.fome = randint(1,100)
        self.saude = saude
        
    def exibir_dados(self):
        linha = '='*11
        print(linha)
        print(f'{"NOME:":<7}{self.nome}\n{"FOME:":<7}{self.fome}\n{"SAUDE:":<7}{self.saude:.0f}')
        print(linha)
        
    def tempo(self):
        tempo = int(input('Digite quantas horas quer avançar: '))
        print(f'Você avançou {tempo} horas.')
        self.fome -= 10 * tempo
        self.saude -= 10 * tempo
        
    def alimentar(self, comida):
        print('Alimentando...')
        self.fome += comida.kcal
        self.saude *= 1.1
        
#EXIBIR DADOS
#TEMPO
#ALIMENTAR

class Comida():
    def __init__(self, nome, kcal):
        self.nome = nome
        self.kcal = kcal
    
class Fini(Comida):
    def __init__(self):
        super().__init__('Fini', 40)
        
class KitKat(Comida):
    def __init__(self):
        super().__init__('KitKat', 20)
        
lista = []

poe1 = Poe('Poe')
poe2 = Poe('Peppa')
poe3 = Poe('Gui')


lista.append(poe1)
lista.append(poe2)
lista.append(poe3)

for i in lista:
    i.exibir_dados()

