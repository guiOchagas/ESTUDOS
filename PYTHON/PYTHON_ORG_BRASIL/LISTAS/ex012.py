from random import randint

idade = []
altura = []
contador = 0


for aluno in range(10):
    idade.append(randint(7, 18))
    altura.append(randint(140, 190))

altura_media = sum(altura) / len(altura)

for aluno in range(10):
    if idade[aluno] >= 13 and altura[aluno] < altura_media:
        contador += 1

print(idade)
print(altura)

print(f"""A altura média da turma é {altura_media:.2f} e a quantidade 
de alunos com mais de 13 anos menores que a média é {contador}""")
