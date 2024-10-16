"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

lista = []
num = 1
print("Digite [ 0 ] para finalizar.")
while num > 0:
    num = int(input(f"Digite um número: "))
    if num > 1000:
        print("Erro, digite um número menor que 1000")
    elif num > 0 and num < 1000:
        lista.append(num)
    

maior = (max(lista))
menor = (min(lista))
soma = maior + menor
print(f"Maior: {maior}\nMenor: {menor}\nSoma: {soma}")
