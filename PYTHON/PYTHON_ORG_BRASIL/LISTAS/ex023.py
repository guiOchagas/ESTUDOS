def conversao(lista):
    lista_conversoes = []
    mebibyte = 1048576
    for item in lista:
        result = item / mebibyte
        lista_conversoes.append(result)
    return lista_conversoes

def porcentagem(lista):
    lista_porcentagens = []
    for item in lista:
        porc = item / sum(lista) * 100
        porc_arrendondada = round(porc, 2)
        lista_porcentagens.append(porc_arrendondada)
    return lista_porcentagens

lista_nomes = ["alexandre", "anderson", "antonio", "carlos", "cesar", "rosemary"]
lista_usage = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
lista_total = dict(zip(lista_nomes, lista_usage))

print(f'{"ACME Inc.":<24}Uso do espaço em disco pelos usuários')
print('-'*65)
print(f"{'Nr.':<5}{'Usuário':<15}{'Espaço utilizado':<21}{'% do uso':<8}")
print()
for i, (nome, usage) in enumerate(lista_total.items()):
    print(f'{i+1:<5}{nome:<15}{conversao(lista_usage)[i]:<8.2f} MB{"          "}{porcentagem(lista_usage)[i]:<6}%')
print()

soma_usage = sum(conversao(lista_usage))
espaco_medio_usage = soma_usage / len(lista_usage)

print(f'Espaço total ocupado: {soma_usage:.2f} MB')
print(f'Espaço médio ocupado: {espaco_medio_usage:.2f} MB')

