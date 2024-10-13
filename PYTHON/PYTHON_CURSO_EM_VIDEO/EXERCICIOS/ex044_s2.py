print(' ='*20)
print('         MAQUININHA DE CARTÃO')
print(' ='*20)
print()
produto = float(input('Por favor, digite o preço do produto: R$'))
dinheiro = produto - (produto * 0.1)
debito = produto - (produto * 0.05)
credito1 = produto
credito2 = produto + (produto * 0.2)
print()
print('==SELECIONE A FORMA DE PAGAMENTO==')
print()
print('1 | Dinheiro\n2 | Débito\n3 | Crédito (Em até 12x)')
print()
sel = int(input('Digite uma das opções: '))
print()
if sel == 1:
    print('O valor do produto é: R${:.2f}'.format(dinheiro))
elif sel == 2:
    print('O valor do produto é: R${:.2f}'.format(debito))
elif sel == 3:
    print('Deseja dividir em quantas vezes?')
    print()
    parc = int(input(''))
    print()
    if parc == 1 or parc == 2:
        print('O valor total do produto é R${:.2f} com {} parcela(s) de {:.2f}'.format(credito1, parc, credito1 / parc))
    elif parc >= 3 and parc <= 12:
        print('O valor total do produto é R${:.2f} com {} parcela(s) de R${:.2f}'.format(credito2, parc, credito2 / parc))
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
