def decorador(func):
    def nova_frase():
        print('Olá! Meu nome é ', end='')
        func()
    return nova_frase



@decorador
def meu_nome():
    print('GUILHERME')


meu_nome()
