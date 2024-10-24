def valor_pag(p, d):
    lista_total = []

    multa = 0.3
    juros_d = 0.01

    total_com_taxas = (p * multa) + (p * juros_d) + p

    if d >= 0:
        lista_total.append(p)
        return f'Valor total a ser pago: {p}'

    elif d < 0:
        lista_total.append(total_com_taxas)
        return f'A fatura está {abs(d)} dias em atraso e o total a ser pago é {total_com_taxas} sendo {p * multa} de multa e {p * juros_d} de juros por dia.'


while True:
    prestacao = float(input('VALOR DA PRESTAÇÃO: '))
    if prestacao == 0:
        print('ENCERRANDO...')
        break

    dia = int(input('DIA DO PAGAMENTO (USE "-" SE ESTIVER VENCIDO): '))
    if dia == 0:
        print('ENCERRANDO...')
        break

    result = valor_pag(prestacao, dia)
    print(result)

