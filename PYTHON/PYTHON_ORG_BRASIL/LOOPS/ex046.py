lista = [7, 8.5, 9, 7.5, 5.5, 3.5]

maior = max(lista)
menor = min(lista)

print(maior, menor)
lista_media = lista

print(lista_media)

lista_media.remove(maior)
lista_media.remove(menor)
        
print(lista_media)

media = sum(lista_media) / len(lista_media)

print(media)
