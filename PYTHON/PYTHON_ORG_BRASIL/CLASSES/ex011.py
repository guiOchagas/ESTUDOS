"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque."""


class Carro():
    def __init__(self, consumo, combustivel=0):
        self.consumo = consumo
        self.combustivel = combustivel

    def andar(self, km):
        print(f'COMBUSTIVEL: {self.combustivel}')
        if self.combustivel == 0:
            print('SEM COMBUSTIVEL :(')
        else:
            print(f'Dirigindo por {km} quilômetros.')
            print('Vruummm...')
            self.combustivel -= km
            
    def adicionarGasolina(self, abastecer):
        print(f'Você abasteceu R${abastecer:.2f} de gasolina')
        self.combustivel = abastecer
                
    def ExibirTanque(self):
        print(f'COMBUSTIVEL DISPONIVEL: {self.combustivel}')
    
bmw = Carro(10)

bmw.adicionarGasolina(100)
bmw.andar(45)
bmw.ExibirTanque()






