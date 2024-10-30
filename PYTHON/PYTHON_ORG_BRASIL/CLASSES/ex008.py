"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?"""



class Macaco():
    def __init__ (self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
        
    def comer(self, comida):
        print(f'O {self.nome} comeu {comida.nome} e consumiu {comida.kcal} calorias.')
        self.bucho += comida.kcal
    
    def verBucho(self):
        pass
    
    def digerir(self):
        pass
    
class Comida():
    def __init__ (self, nome, kcal):
        self.nome = nome
        self.kcal = kcal
        
        
class Banana(Comida):
    def __init__ (self):
        super().__init__('Banana', 200)
        


class Morango(Comida):
    def __init__ (self):
        super().__init__('Morango', 100)
    
        
        
class Maca(Comida):
    def __init__ (self):
        super().__init__('Maçã', 400)



macaco = Macaco('Cesar', 0)
banana = Banana()

macaco.comer(banana)



