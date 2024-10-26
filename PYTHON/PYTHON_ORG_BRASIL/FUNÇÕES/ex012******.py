"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante."""


def desenha_moldura(linhas=1, colunas=1):
    # Verifica e ajusta os valores para a faixa de 1 a 20
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    # Desenha o retângulo
    for i in range(linhas):
        if i == 0 or i == linhas - 1:  # Linha superior ou inferior
            print('+' + '-' * (colunas - 2) + '+')
        else:  # Linhas intermediárias
            print('|' + ' ' * (colunas - 2) + '|')


desenha_moldura(10,20)
