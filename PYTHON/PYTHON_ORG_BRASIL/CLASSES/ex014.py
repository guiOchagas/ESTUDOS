"""Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.


Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.

"""


class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def exibir_dados(self):
        print(f'Nome: {self.nome} | Salário: R${self.salario:.2f}')
        
    def aumentar_salario(self):
        taxa = float(int(input('DIGITE O AUMENTO EM PORCENTAGEM: ')))
        self.salario += self.salario * (taxa / 100)

funcionario1 = Funcionario('Gui', 6000)

funcionario1.exibir_dados()

funcionario2 = Funcionario('Sarah', 10000)

funcionario2.exibir_dados()

funcionario1.aumentar_salario()
funcionario1.exibir_dados()

