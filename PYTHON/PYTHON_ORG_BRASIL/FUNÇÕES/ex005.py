"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""


def conversao(hora, minuto):
    if hora == 0 and minuto == 0:
        hora += 12
        return f'{hora}:{minuto}0AM'
    
    elif hora == 0:
        hora += 12
        return f'{hora}:{minuto}AM'
        
    elif 1 <= hora <= 9:
        if minuto == 0:
            return f'0{hora}:{minuto}0AM'
        else:
            return f'0{hora}:{minuto}AM'
        
    elif 10 <= hora <= 11:
        if minuto == 0:
            return f'{hora}:{minuto}0AM'
        else:
            return f'{hora}:{minuto}AM'
        
    elif hora == 12:
        if minuto == 0:
            return f'{hora}:{minuto}0PM'
        else:
            return f'{hora}:{minuto}PM'
            
    elif 13 <= hora <= 21:
        hora += -12
        if minuto == 0:
            return f'0{hora}:{minuto}0PM'
        else:
            return f'0{hora}:{minuto}PM'
            
    elif 22 <= hora <= 23:
        hora += -12
        if minuto == 0:
            return f'{hora}:{minuto}0PM'
        else:
            return f'{hora}:{minuto}PM'

hora = int(input('HORA: '))
minuto = int(input('MINUTO: '))

horario = conversao(hora, minuto)
print(horario)
