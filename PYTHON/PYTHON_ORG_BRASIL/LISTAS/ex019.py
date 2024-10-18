"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""


titulo = ('TABELA DOS SISTEMAS OPERACIONAIS')
print(titulo)
print('=' * len(titulo))
print("""1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro""")
print('=' * len(titulo))

lista_votos = []
sistemas = ["Windowns", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

while True:
    votos = int(input('Escolha seu voto: '))
    if 0 < votos < 7:
        lista_votos.append(votos)
    elif votos >= 7:
        print('Opção inválida.')
    else:
        break
    
# Separação dos votos por sistema operacional
contador_votos = [0] * 6
for item in lista_votos:
    contador_votos[item - 1] += 1
    
# Calcular a porcentagem
print(f'{"SISTEMA":<10}{"VOTOS":^10}{"%":>10}')
for sistema in range(6):
    if contador_votos[sistema] > 0:
        porcentagem = (contador_votos[sistema] / len(lista_votos) * 100)
        print(f'{sistemas[sistema]:<10}{contador_votos[sistema]:^10}{porcentagem:>10.2f}')
