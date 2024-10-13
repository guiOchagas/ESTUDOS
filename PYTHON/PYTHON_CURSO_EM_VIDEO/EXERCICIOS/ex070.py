print('=' * 30)
print('{: ^30}'.format('CADASTRAR PRODUTOS'))
print('=' * 30)

total = cart = mil = 0
barato = ' '
preço_barato = float('inf')  # Inicializa com um valor alto para comparar depois

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    
    total += preço
    cart += 1
    if preço > 1000:
        mil += 1
    if preço < preço_barato:  # Corrige a lógica do produto mais barato
        preço_barato = preço
        barato = produto
    
    print()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).upper().strip()
    
    if continuar == 'N':  # Corrige a lógica de finalização
        print('Finalizando...')
        break

print()
print(f"""O total gasto na compra foi R${total:.2f}
Produtos que custam mais de R$1000: {mil}
O produto mais barato foi: {barato}""")
