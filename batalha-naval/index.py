import random

perguntas_iniciciais_validas = False
qtd_jogadores = 0
dificuldade = {}
altura_tabuleiro = 10
largura_tabuleiro = 10
tabuleiro1 = []
tabuleiro2 = []

while perguntas_iniciciais_validas == False:
	resposta = int(input('Quantos jogadores irão jogar? (1/2)\n'))

	if (resposta == 1):
		qtd_jogadores = 1
	elif (resposta == 2):
		qtd_jogadores = 2	
	else:
		print('Entre com um valor válido!')

	resposta = int(input('\nSelecione a dificuldade:\n 1- Normal\n 2- Difícil\n'))

	if (resposta == 1):
		dificuldade = {
			'tipo': 1,
			'qtd_bombas': 30,
			'navios': 20
		}
	elif (resposta == 2):
		dificuldade = {
			'tipo': 2,
			'qtd_bombas': 200,
			'navios': 50
		}

		altura_tabuleiro = 20
		largura_tabuleiro = 20
	else:
		print('Entre com um valor válido!')

	perguntas_iniciciais_validas = True

if(qtd_jogadores == 1):
	tabuleiro1 = [[0 for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
elif(qtd_jogadores == 2):
	tabuleiro1 = [[0 for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	tabuleiro2 = [[0 for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]

for i in range(0, 29):
	posicao_altura = random.randint(0, altura_tabuleiro - 1)		
	posicao_largura = random.randint(0, largura_tabuleiro - 1)

	tabuleiro1[posicao_altura][posicao_largura] = 'x'

print(tabuleiro1)
