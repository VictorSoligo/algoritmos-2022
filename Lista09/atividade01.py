numeros = []
primos = []
posicoes = []

def e_primo(numero):
	for val in range(2, numero):
		if numero % val == 0:
			return False

	return True

for i in range(0, 9):
	numero = int(input('Digite o número:\n'))
	numeros.append(numero)

	if (e_primo(numero)):
		primos.append(numero)
		posicoes.append(i)

for j in range(0, len(primos)):
  print(f'O número {primos[j]} está na posição  {posicoes[j]}')

for primo in primos:
  posicao = numeros.index(primo)
  print(f'O primo {primo} está na posição {posicao}')
