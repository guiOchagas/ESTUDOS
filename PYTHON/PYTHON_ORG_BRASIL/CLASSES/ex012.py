"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""


class ContaInvestimento():
    def __init__(self, saldo, juros):
        self.saldo = saldo
        self.juros = juros
        
    def add_juros(self):
        self.saldo += self.saldo * (self.juros / 100)
    
    def exibir_conta(self):
        print(f'O saldo atual é R${self.saldo} e a taxa juros é: {self.juros}%.')
        

poupanca = ContaInvestimento(1000, 10)
poupanca.add_juros() #1
poupanca.add_juros() #2
poupanca.add_juros() #3
poupanca.add_juros() #4
poupanca.add_juros() #5

poupanca.exibir_conta()
