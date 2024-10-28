"""Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

def verificar_e_formatar(tel):
    
    def verificador(tel):
        return len(tel) == 11
    
    def formatar(tel):
        if verificador(tel): 
            tel_formatado = f'({tel[:2]}){tel[2:7]}-{tel[7:]}'
            return tel_formatado
        else:
            return f'ERROR'
            
    return verificador(tel), formatar(tel)
    
telefone = '12988629035'

test = verificar_e_formatar(telefone)


print(test)
