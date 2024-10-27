"""Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO"""


nome = 'GUILHERME'

for letra in range(1, len(nome) + 1):
    print(nome[:letra])

