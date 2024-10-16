"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

check = []
sim = nao = 0
result = "DE BOA"

check.append(str(input('Telefonou para a vítima? ')))
check.append(str(input('Esteve no local do crime? ')))
check.append(str(input('Mora perto da vítima? ')))
check.append(str(input('Devia para a vítima? ')))
check.append(str(input('Já trabalhou com a vítima? ')))

for resp in check:
    if resp == "s":
        sim += 1
    if resp == "n":
        nao += 1

if sim == 2:
    result = "SUSPEITO"
if sim > 3 or sim < 4:
    result = "CÚMPLICE"
if sim == 5:
    result = "ASSASSINO"
if sim < 2:
    result = "INOCENTE"
    
print(result)
print(check)
print(sim)
