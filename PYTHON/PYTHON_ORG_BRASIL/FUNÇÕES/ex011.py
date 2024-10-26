"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados."""


from random import randint, shuffle

def embaralha(palavra):
    lista_palavra = list(palavra)
    shuffle(lista_palavra)
    return ''.join(lista_palavra).upper()

while True:
    result = str(input('Digite uma palavra: '))
    print(embaralha(result))
    if result == '0':
        break
