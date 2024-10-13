from time import sleep

#APRESENTAÇÃO
print('='*30)
print('{:^30}'.format('CALCULADORINHA'))
print('='*30)
print()

#VARIÁVEIS
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
select = 0

#ESTRUTURA DE REPETIÇÃO
while select != 5:

    #MENU DE OPÇÕES
    print()
    print('='*30)
    print('{: ^30}'.format('SELECIONE UMA OPÇÃO'))
    print('='*30)
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] ENCERRAR""")
    print()
    
    #CONDIÇÕES
    select = int(input('DIGITE UMA OPÇÃO: '))
    print()
    if select == 1:
        print(f'A soma entre {n1} + {n2} é = {n1 + n2}')
    elif select == 2:
        print(f'A multiplicação entre {n1} x {n2} é = {n1 * n2}')
    elif select == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o {n2}')
        else:
            print(f'O número {n2} é maior que o {n1}')
    elif select == 4:
        print('Digite outros valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif select == 5:
        print('ENCERRANDO...')
        sleep(2)
    else:
        print('OPÇÃO INVÁLIDA.')
print()
print('ATÉ A PRÓXIMA!')
