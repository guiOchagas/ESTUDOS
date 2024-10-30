"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class ContaCorrente():
    def __init__ (self, num, nome, saldo=0):
        self.num = num
        self.nome = nome
        self.saldo = saldo
        
    def AlterarNome(self, nome):
        self.nome = nome
    
    def Deposito(self, saldo):
        self.saldo += saldo
        
    def Saque(self, saldo):
        self.saldo -= saldo



pessoa = ContaCorrente(12345, 'Gui', 6000)
print(pessoa.num, pessoa.nome, pessoa.saldo)

pessoa.AlterarNome('Sarah')
print(pessoa.num, pessoa.nome, pessoa.saldo)

pessoa.Deposito(10000)
print(pessoa.num, pessoa.nome, pessoa.saldo)

pessoa.Saque(20000)
print(pessoa.num, pessoa.nome, pessoa.saldo)
