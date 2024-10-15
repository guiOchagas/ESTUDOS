"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
"""
from time import sleep

print('TABUADA')

while True:
    user = int(input("Escolha um número: "))
    print(f"Tabuada de {user}:")

    for n in range(1,11):
        sleep(0.5)
        print(f"{user} x {n} = {user*n}")
    sleep(1)
    resp = str(input("Continuar? [S/N] ")).upper()
    if resp == 'N':
        break
print("SAINDO...")
sleep(2)
print("ATÉ A PRÓXIMA!")
