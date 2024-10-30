"""Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo."""

import random 

def embaralhador():
    words = ['sarah', 'guilherme', 'alana', 'liam', 'samuel', 'ulisses', 'lilian', 'cristina', 'andre', 'igor', 'andressa', 'vinicius', 'noah']
    palavra_misterio = random.choice(words)
    indice = words.index(palavra_misterio)
    palavra_resposta = words[indice]
    palavra_misterio = list(palavra_misterio)
    random.shuffle(palavra_misterio)
    return ' '.join(palavra_misterio), palavra_resposta, indice

misterio, resposta, indice = embaralhador()
cont = 0
resposta = resposta.upper()

print(misterio, resposta, indice)

title = 'ADVINHE A PALAVRA'

print(f'{title}\n{"="*len(title)}')
print(misterio.upper())

for c in range(3):
    resp = str(input(f'{c + 1}º de 6 tentativas: ')).upper()
    cont += 1
    if resp == resposta:
        print('ACERTOU')
        break
    elif resp != resposta:
        if c == 2:
            print('VOCÊ ATINGIU 6 TENTATIVAS E PERDEU')
            break
        else:
            print('VOCÊ ESTÁ QUASE LÁ')

        
print(f'Você utilizou {cont}/3 tentativas e acertou.')
