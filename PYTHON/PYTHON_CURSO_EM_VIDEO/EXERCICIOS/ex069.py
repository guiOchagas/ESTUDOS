homem = mulher = maior = menor = cont = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: ')).upper()
    
    if idade >= 18: #MAIOR DE IDADE
        maior += 1
    
    if sexo == 'M': #HOMENS
        homem += 1
        
    if sexo == 'F': #MULHERES
        mulher += 1
        
    if sexo == 'F' and idade < 18:
        menor += 1

    cont += 1

    print()
    go = ' '
    while go not in 'SN':
        go = str(input('Deseja continuar? [S/N]: ')).upper()
    print()
    if go == 'N':
        break

print()
print(f"""PESSOAS CADASTRADAS: {cont}
MAIOR DE IDADE: {maior}
HOMENS: {homem}
MULHERES: {mulher}
MULHERES -18: {menor}""")
