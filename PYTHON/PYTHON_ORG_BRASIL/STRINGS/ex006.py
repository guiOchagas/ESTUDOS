"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973."""

#SOLUÇÃO 1
def conv_mes(mes):
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    mes_ind = int(mes[3]) + int(mes[4])
    result = meses[mes_ind - 1]
    return result

nasc = '01/04/1999'
print(f'Data de nascimento: {nasc}')
print(f'Você nasceu em {nasc[:2]} de {conv_mes(nasc)} de {nasc[6:]}')

print()
print()
print()

#SOLUÇÃO 2
def converte_mes(data):
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    
    dia = data[:2]
    mes = int(data[3:5])
    ano = data[6:]
    
    mes_ext = meses[mes - 1]
    
    return f'{dia} de {mes_ext.capitalize()} de {ano}'
    
nasc = '01/04/1999'
print(converte_mes(nasc))
