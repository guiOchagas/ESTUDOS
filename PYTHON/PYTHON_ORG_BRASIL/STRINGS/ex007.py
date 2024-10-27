"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""


frase = 'Gui Chagas'

space = letras = 0
vogais = {}

for c in frase:
    if c == ' ':
        space += 1
    if c != ' ':
        letras += 1
    if c in 'aeiou':
        if c in vogais:
            vogais[c] += 1
        else:
            vogais[c] = 1
            
print(space, letras, vogais)
        
