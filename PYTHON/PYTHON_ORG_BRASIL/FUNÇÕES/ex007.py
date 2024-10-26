"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""


def contar_digito(num):
    conversao = str(num)
    return len(str(num))


numero = 100000000
numero_convertido = contar_digito(numero)
print(numero_convertido)
