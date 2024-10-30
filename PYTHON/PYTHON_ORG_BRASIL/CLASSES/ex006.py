"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""


class Televisor():
    def __init__ (self, canal=10, volume=50):
        self.canal = canal
        self.volume = volume
        
    def TrocarCanal(self, canal):
        if canal < 1 or canal > 100:
            print('Este canal não existe.')
        else:
            self.canal = canal
        
    def AumentarVolume(self, volume):
        if volume == 100:
            self.volume = volume
            print('MÁXIMO')
        else:
            self.volume = volume
        
    def DiminuirVolume(self, volume):
        if volume == 0:
            self.volume = volume
            print('MUDO')
        else:
            self.volume = volume
        

tv = Televisor()
print(f'Canal: {tv.canal}\nVolume: {tv.volume}')
print()

tv.TrocarCanal(150)
print(f'Canal: {tv.canal}\nVolume: {tv.volume}')
print()

tv.AumentarVolume(100)
print(f'Canal: {tv.canal}\nVolume: {tv.volume}')
print()

tv.DiminuirVolume(80)
print(f'Canal: {tv.canal}\nVolume: {tv.volume}')
print()
