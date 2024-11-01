"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""



class bombaCombustivel():
    def __init__(self, preco=3.5, tipo='Gasolina', qtd=1000):
        self.preco = preco
        self.tipo = tipo
        self.qtd = float(qtd)

    def abastecerPorValor(self):
        valor = float(input('QUAL VALOR DESEJA ABASTECER? '))
        litros = valor / self.preco
        self.qtd -= litros
        print()
        print(f'Abastecido => R${valor:.2f} = {litros:.2f} litros.')
    
    def abastecerPorLitro(self):
        litros = float(input('QUANTOS LITROS DESEJA ABASTECER? '))
        valor = litros * self.preco
        self.qtd -= litros
        print()
        print(f'Abastecido => {litros:.2f} litros = R${valor:.2f}')
        
    def alterarValor(self):
        novo_valor = float(input('DIGITE UM NOVO VALOR PARA ABASTECER: '))
    
    def alterarCombustivel():
        pass
    
    def alterarQuantidadeCombustivel():
        pass
    
bomba = bombaCombustivel()
print(bomba.qtd)
print()



