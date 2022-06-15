# primeiro indice é a linha, segundo a coluna
import random

# Variáveis

perguntas_iniciciais_validas = False
jogo_rodando = True

qtd_jogadores = 0
dificuldade = 0
config_dificuldade = {}

altura_tabuleiro = 10
largura_tabuleiro = 10

tabuleiro1 = []
tabuleiro2 = []

tabuleiro_jogador1 = []
tabuleiro_jogador2 = []

pontuacao_jogador1 = 0
pontuacao_jogador2 = 0

# Funções

def print_tabuleiro_jogador1():
  print('')
  for line in tabuleiro_jogador1:
    print ('  '.join(map(str, line)))

def print_tabuleiro_jogador2():
  print('')	
  for line in tabuleiro_jogador2:
    print ('  '.join(map(str, line)))

def preencher_bombas(nro_jogadores):
	quantidade_bombas = config_dificuldade['qtd_bombas']
	bombas_no_campo = 0

	while quantidade_bombas != bombas_no_campo:
		linha = random.randint(0, altura_tabuleiro - 1)		
		coluna = random.randint(0, largura_tabuleiro - 1)

		posicao_tabuleiro = tabuleiro1[linha][coluna]

		if posicao_tabuleiro != 'B' and posicao_tabuleiro != 'N':
			tabuleiro1[linha][coluna] = 'B'
			bombas_no_campo += 1

	if nro_jogadores == 2:
		bombas_no_campo = 0

		while quantidade_bombas != bombas_no_campo:
			linha = random.randint(0, altura_tabuleiro - 1)		
			coluna = random.randint(0, largura_tabuleiro - 1)

			if posicao_tabuleiro != 'B' and posicao_tabuleiro != 'N':
				tabuleiro2[linha][coluna] = 'B'
				bombas_no_campo += 1

def preencher_navios(nro_jogadores):
	quantidade_navios = config_dificuldade['qtd_navios']
	navios_no_campo = 0

	while quantidade_navios != navios_no_campo:
		coluna = random.randint(0, altura_tabuleiro - 1)		
		linha = random.randint(0, largura_tabuleiro - 1)

		posicao_tabuleiro = tabuleiro1[linha][coluna]
		ultima_coluna = (largura_tabuleiro - 1)

		if posicao_tabuleiro != 'N':
			if((coluna + 2) < ultima_coluna) and ((linha - 2) > 0):
				for v in range(2):
					tabuleiro1[linha][coluna + v] = 'N'
					
				navios_no_campo += 2

	if nro_jogadores == 2:
		navios_no_campo = 0

		while quantidade_navios != navios_no_campo:
			coluna = random.randint(0, altura_tabuleiro - 1)		
			linha = random.randint(0, largura_tabuleiro - 1)

			posicao_tabuleiro = tabuleiro2[linha][coluna]
			ultima_coluna = (largura_tabuleiro - 1)

			if posicao_tabuleiro != 'N':
				if((coluna + 2) < ultima_coluna) and ((linha - 2) > 0):
					for v in range(2):
						tabuleiro2[linha][coluna + v] = 'N'

					navios_no_campo += 2
	
#Início

while perguntas_iniciciais_validas == False:
	while (qtd_jogadores == 0):
		resposta = int(input('Quantos jogadores irão jogar? (1/2)\n'))

		if (resposta == 1):
			qtd_jogadores = 1
		elif (resposta == 2):
			qtd_jogadores = 2	
		else:
			print('\nEntre com um valor válido!\n')

	while (dificuldade == 0):
		resposta = int(input('\nSelecione a dificuldade:\n 1- Normal\n 2- Difícil\n'))

		if (resposta == 1):
			dificuldade = 1

			config_dificuldade = {
				'nivel': 1,
				'qtd_bombas': 30,
				'qtd_navios': 20,
				'nro_jogadas': 10,
			}
		elif (resposta == 2):
			dificuldade = 2

			config_dificuldade = {
				'nivel': 2,
				'qtd_bombas': 100,
				'qtd_navios': 50,
				'nro_jogadas': 20,			
			}

			altura_tabuleiro = 20
			largura_tabuleiro = 20
		else:
			print('\nEntre com um valor válido!\n')

	perguntas_iniciciais_validas = True

if(qtd_jogadores == 1):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	tabuleiro_jogador1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]	
elif(qtd_jogadores == 2):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	tabuleiro2 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]

	tabuleiro_jogador1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]	
	tabuleiro_jogador2 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]		

preencher_navios(qtd_jogadores)
preencher_bombas(qtd_jogadores)

if(qtd_jogadores == 1):
	print('\nO jogo irá iniciar')

	for line123 in tabuleiro1:
		print ('  '.join(map(str, line123)))

	escolhendo_linha = True
	escolhendo_coluna = True
	jogada_valida = False

	while jogo_rodando == True:
		for i in range(config_dificuldade['nro_jogadas']):
			print_tabuleiro_jogador1()

			jogada_valida = False		
			
			escolhendo_linha = True
			escolhendo_coluna = True

			posicao_linha = 0
			posicao_coluna = 0

			while jogada_valida == False:
				while escolhendo_linha == True:
					posicao_linha = int(input(f'\nEm qual linha você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_linha >= 0) and (posicao_linha <= (largura_tabuleiro - 1)):
						escolhendo_linha = False
					else:
						print('\nDigite um valor válido!\n')
						
				while escolhendo_coluna == True:
					posicao_coluna = int(input(f'\nEm qual coluna você deseja jogar: (0-{largura_tabuleiro - 1})\n'))

					if (posicao_coluna >= 0) and (posicao_coluna <= (altura_tabuleiro - 1)):
						escolhendo_coluna = False
					else:
						print('\nDigite um valor válido!')

				if(tabuleiro1[posicao_linha][posicao_coluna] != 'Ç'):
					if(tabuleiro1[posicao_linha][posicao_coluna] == 'N'):
						pontuacao_jogador1 += 10

						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'X'						

						jogada_valida = True
					elif(tabuleiro1[posicao_linha][posicao_coluna] == '-'):
						pontuacao_jogador1 = pontuacao_jogador1

						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'X'						

						jogada_valida = True
					else:
						print('BOMBA')

						tabuleiro1[posicao_linha][posicao_coluna] = 'Ç'
						tabuleiro_jogador1[posicao_linha][posicao_coluna] = 'X'
						
						jogada_valida = True

						jogo_rodando = False				
				else:
					jogada_valida = False			
		
		print_tabuleiro_jogador1()
		jogo_rodando = False		

# Print

print('')

for line123 in tabuleiro1:
  print ('  '.join(map(str, line123)))

print('')
print('')

print(pontuacao_jogador1)

print('')
print('')

# for line123 in tabuleiro2:
#   print ('  '.join(map(str, line123)))