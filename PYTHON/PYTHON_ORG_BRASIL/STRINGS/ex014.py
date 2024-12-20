"""Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak."""


leet = {"A": '4', "B": '8', "C": '(', "E": '3', "G": '9', "I": '1', "O": '0', "S": '$', "T": '7', "Z": '2'}

user = str(input('Digite um texto para traduzir: '))
trad = list(user)
print()


for i in range(len(trad)):
    if trad[i].upper() in leet:
        trad[i] = leet[trad[i].upper()]
        
print(f'Você digitou: {user.upper()}\nTradução em leet: {"".join(trad).upper()}')
