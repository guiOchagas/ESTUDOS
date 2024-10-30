"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""



class Tamagushi():
    def __init__ (self, tempo=0, nome='Poe', fome=100, saude=100, idade=1):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tempo = tempo
    
    
    def Humor(self):
        if self.fome > 70 and self.saude > 70:
            return 'Feliz'
        
        elif self.fome > 50 and self.saude > 50:
            return f'To ficando com fome'
        
        elif self.fome > 30 and self.saude > 30:
            return 'Quero comer'
        
        elif self.fome >= 10 and self.saude >= 10:
            return 'TO PASSANDO MAL DE FOME'
        
        elif self.fome == 0 and self.saude == 0:
            return f'VOCÊ DEIXOU O {self.nome} MORRER.'
        
            
    def AvancarTempo(self, tempo):
        print(f'Você avançou {tempo} hora(s)')
        self.tempo += tempo
        self.fome -= 10 * tempo
        self.saude -= 10 * tempo
        
        
    def MostrarDados(self):
        print(f'Nome: {self.nome}\nFome: {self.fome}\nSaude: {self.saude}\nIdade: {self.idade}\nTempo: {self.tempo}\nHumor: {self.Humor()}')
    
        
        

poe = Tamagushi()

poe.MostrarDados()

print()
poe.AvancarTempo(10)
poe.MostrarDados()
