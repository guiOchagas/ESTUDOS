''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

media = 0
idade_velho = 0
mulheres = 0
contador = 0
soma_idades = 0


for c in range(7):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    print()
    
    if sexo == 'M':
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
        
    elif sexo == 'F':
        if idade < 20:
            mulheres += 1
    
    contador += 1
    soma_idades += idade
    media = (soma_idades / contador)

print(f'A idade média do grupo cadastrado é de {int(media)} anos')
print(f'O homem mais velho cadastrado é o {nome_velho} com {idade_velho} anos')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')

