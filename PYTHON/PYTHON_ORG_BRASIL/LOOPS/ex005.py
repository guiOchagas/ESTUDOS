"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

print('CALCULO E COMPARAÇÃO POPULACIONAL')

while True:
    pais_a = int(input('POPULAÇÃO A: '))
    taxa_a = float(input('TAXA DE NATALIDADE ANUAL: '))

    pais_b = int(input('POPULAÇÃO B: '))
    taxa_b = float(input('TAXA DE NATALIDADE ANUAL: '))

    cont = 0

    while pais_a <= pais_b:
        pais_a += pais_a * taxa_a
        pais_b += pais_b * taxa_b
        cont += 1

    print(
        f'Serão {cont} anos necessários para que o país A ultrapasse o país B é. No final a população do país A será de {pais_a} e do país B será de {pais_b}.')

    resp = str(input('FAZER OUTRA CONSULTA? [S/N] ')).upper()
    if resp == 'N':
        break
