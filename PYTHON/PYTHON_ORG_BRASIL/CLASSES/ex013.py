"""Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe."""


class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def exibir_dados(self):
        print(f'Nome: {self.nome} | Salário: {self.salario}')
        

funcionario1 = Funcionario('Gui', 6000)

funcionario1.exibir_dados()

funcionario2 = Funcionario('Sarah', 10000)

funcionario2.exibir_dados()
