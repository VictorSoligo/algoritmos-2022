import random
import math

vetor1 = []
vetor2 = []

for i in range(8):
  vetor1.append(random.randint(0, 1000))
  vetor2.append(random.randint(0, 1000))

def calcula_distacia_euclidiana(vetor1, vetor2):
  soma = 0

  for j in range(len(vetor1)):
    d = vetor1[j] - vetor2[j]
    soma += d * d

  print(f'Vetor 1: {vetor1}')
  print(f'Vetor 2: {vetor2}')
  print(f'\nDistância euclidiana: {math.sqrt(soma)}')

  return math.sqrt(soma)

calcula_distacia_euclidiana(vetor1, vetor2)
