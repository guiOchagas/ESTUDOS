"""Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você faz um "natural" e ganha. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perde. Se, na primeira jogada, você fizer 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar esse número novamente. Você perde, no entanto, se tirar um 7 antes de tirar esse Ponto novamente."""


from random import randint


def craps():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    result = dado1 + dado2
    if result in (7, 11):
        
        return f'Você tirou {result} e fez um "NATURAL" e GANHOU!'
        
    
    elif result in (2, 3, 12):
        
        return f'Você tirou {result} e fez um "CRAPS" e PERDEU!'
        

    elif result in (4, 5, 6, 8, 9, 10):
        print(f'Você tirou {result} e fez um "PONTO", jogue mais uma vez até acertar o número {result} novamente.')
        
        while result != 7:
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            novo_result = dado1 + dado2
            
            if novo_result == 7:
                print(f'Você tirou {novo_result} e PERDEU!')
                break
            
            elif result == novo_result:
                print(f'Você tirou {novo_result} novamente e GANHOU!')
                break
            
            elif novo_result != 7:
                print(f'Você tirou {novo_result}, continue jogando. Até tirar {result} novamente.')

jogo = craps()
print(jogo)
