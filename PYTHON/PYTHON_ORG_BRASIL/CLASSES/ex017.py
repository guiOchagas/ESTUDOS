"""Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio."""

from random import randint


class Poe:

    def __init__(self, nome, saude=100):
        self.nome = nome
        self.fome = randint(1, 100)
        self.saude = saude

    def exibir_dados(self):
        linha = '=' * 11
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


# EXIBIR DADOS
# TEMPO
# ALIMENTAR

class Comida:
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

poe1 = Poe('Gui')
poe2 = Poe('Sarah')
poe3 = Poe('Samu')

fini = Fini()

lista.append(poe1)
lista.append(poe2)
lista.append(poe3)

for i in lista:
    i.alimentar(fini)
    print(i.nome, i.fome)

