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
