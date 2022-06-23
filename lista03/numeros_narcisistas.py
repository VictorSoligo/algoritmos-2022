import math

resposta = input('Digite um número:\n')

def e_narcisista(numero):
  soma = 0
  len_numero = len(numero)
  numero_int = int(numero)

  for algarismo in numero:
    numero = int(algarismo)

    potencia = math.pow(numero, len_numero)

    soma += potencia

  if soma == numero_int:
    return True
  else:
    return False

if e_narcisista(resposta):
  print(f'\nO número {resposta} é narcisista')
else:
  print(f'\nO número {resposta} não é narcisista')
