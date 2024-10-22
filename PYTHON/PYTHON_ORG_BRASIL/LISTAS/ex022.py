"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:"""

quantidade_de_mouses = 50

problemas = {"Esfera": 0, "Limpeza": 0, "Cabo": 0, "Quebrado": 0}

print("""Selecione um problema:
1 - Esfera
2 - Limpeza
3 - Cabo
4 - Quebrado""")

while True:
    
    print(quantidade_de_mouses)
    analise = int(input('Digite uma opção ou [0] para sair: '))
    
    if 0 < analise <= 4:
        quantidade_de_mouses -= 1
    
    if analise > 4:
        print('ERRO, digite uma opção válida.')

    if analise == 1:
        problemas["Esfera"] += 1
    
    elif analise == 2:
        problemas["Limpeza"] += 1
    
    elif analise == 3:
        problemas["Cabo"] += 1

    elif analise == 4:
        problemas["Quebrado"] += 1
        
    elif analise == 0:
        break

total = sum(problemas.values())

lista_porcentagens = []

for item in problemas.values():
    porcentagem = (item * 100) / total
    lista_porcentagens.append(porcentagem)

print(f"{'Situação':<20}{'Quantidade':^10}{'Percentual':>20}")

for i, (chave, valor) in enumerate(problemas.items()):
    if i < len(lista_porcentagens):
        print(f"{i+1} - {chave:<20}{valor:^10}{lista_porcentagens[i]:>20.0f}%")

    
    
    
    
    
    
    
