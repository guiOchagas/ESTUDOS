def notas(n):
    nota = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if 0 <= nota['média'] <= 4:
        nota['situação'] = 'Reprovado'
    elif 4 < nota['média'] <= 7:
        nota['situação'] = 'Recuperação'
    elif 7 < nota['média'] <= 10:
        nota['situação'] = 'Aprovado'
    return nota

lista = []
qtd = int(input('Deseja adicionar quantas notas? '))
for c in range(qtd):
    notes = int(input(f'Digite a {c+1}º nota: '))
    lista.append(notes)

result = notas(lista)
print(result)
