from time import sleep
sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'M,F,m,f':
    sexo = str(input('Error, try again: ' )).strip().upper()[0]
print()
print(f'Sexo {sexo} registrado com sucesso.')

sleep(1)

print()
idade = int(input('Digite sua idade: '))
print()
if idade < 18:
    print('Acesso negado!')
else:
    nome = str(input('Qual o seu nome? '))
    if nome == 'Gui':
        print('Você conseguiu!')
    else:
        print('Continue estudando, você vai conseguir!')
