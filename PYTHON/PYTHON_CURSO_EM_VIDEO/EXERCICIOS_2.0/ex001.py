main = True

# menu
def exibir_menu():
    print("""
1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa""")

    print()

def execute(x):
    
    # opção 1
    def somar(a, b):
        print(a + b)
        print()
    
    # opção 2 
    def multiplicar(a, b):
        print(a * b)
        print()
    
    # opção 3
    def maior(a, b):
        if a > b:
            print(a)
        else:
            print(b)
        print()
    
    # opção 4
    def novos_num():
        print()
        pass
    

    
    if option == 1:
        somar(valor1, valor2)
    elif option == 2:
        multiplicar(valor1, valor2)
    elif option == 3:
        maior(valor1, valor2)
    elif option == 4:
        novos_num()
    elif option == 5:
        global main
        main = False


while main:
    valor1 = int(input('valor 1: '))
    valor2 = int(input('valor 2: '))
    
    exibir_menu()
    
    option = int(input('Selecione uma opção: '))
    
    execute(option)
    
    
    
    
