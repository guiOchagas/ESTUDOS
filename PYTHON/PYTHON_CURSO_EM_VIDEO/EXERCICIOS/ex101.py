def voto(ano):
  from datetime import date
  ano_atual = date.today().year
  idade_voto = 18
  idade = ano_atual - ano
  if idade < idade_voto:
    return f'Com {idade} anos: NÃO VOTA.'
  elif idade >= idade_voto and idade <= 60:
    return f'Com {idade} anos: OBRIGATÓRIO'
  else:
    return f'Com {idade} anos: OPCIONAL'

resp = int(input('Em que ano você nasceu? '))

print(voto(resp))
