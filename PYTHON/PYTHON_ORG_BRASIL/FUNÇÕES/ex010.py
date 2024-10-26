"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""


def mes_por_extenso(data):
    
    conversao_dia = int(data[0] + data[1])
    
    conversao_mes = int(data[3] + data[4])
    
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    
    if conversao_dia < 1 or conversao_dia > 31:
        return f'Erro, digite um DIA válido'
        
    if conversao_mes < 1 or conversao_mes > 12:
        return f'Erro, digite um MÊS válido'
    
    else:
        return f'{data[:2]} de {meses[conversao_mes - 1]} de {data[6:]}'
    
    

receba = str(input('Digite uma data no formato DD/MM/AAAA: '))

result = mes_por_extenso(receba)
print(result)
