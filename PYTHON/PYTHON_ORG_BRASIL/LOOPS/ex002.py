#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = str(input('Login: '))

while True:
    password = str(input('Senha: '))
    if login == password:
        print('O login e senha não podem ser iguais. Escolha outra senha.')
    else:
        print('ENTRANDO...')
        break
