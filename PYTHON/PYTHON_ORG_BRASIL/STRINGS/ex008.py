"""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""

def retirar_espaco(word):
    sem_espacos = word.replace(' ', '')
    return sem_espacos

def inverter(word):
    invert = ''.join(reversed(word))
    return invert
    
def verificar(word1, word2):
    if word1.lower() == word2.lower():
        return f'{word1} e {word2} são palindromos.'
    else:
        return f'{word1} e {word2} não são palindromos.'
        
palindromo = 'kaiak'
verificacao = 'K A I A K'

n1 = retirar_espaco(palindromo)
n2 = retirar_espaco(verificacao)

result = verificar(inverter(n1), n2)
print(result)
