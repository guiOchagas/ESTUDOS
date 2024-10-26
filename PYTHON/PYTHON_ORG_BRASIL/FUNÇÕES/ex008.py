"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

"""


def inverter_num(num):
    conversao = list(str(num))
    conversao.reverse()
    return num, ''.join(conversao)
    
print(inverter_num(127))
