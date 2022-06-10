# primeiro indice é a linha, segundo a coluna
import random

# Variáveis

perguntas_iniciciais_validas = False
qtd_jogadores = 0
dificuldade = 0
config_dificuldade = {}
altura_tabuleiro = 10
largura_tabuleiro = 10
tabuleiro1 = []
tabuleiro2 = []

# Funções

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
	
# Início

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
				'qtd_navios': 20
			}
		elif (resposta == 2):
			dificuldade = 2

			config_dificuldade = {
				'nivel': 2,
				'qtd_bombas': 100,
				'qtd_navios': 50
			}

			altura_tabuleiro = 20
			largura_tabuleiro = 20
		else:
			print('\nEntre com um valor válido!\n')

	perguntas_iniciciais_validas = True

if(qtd_jogadores == 1):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
elif(qtd_jogadores == 2):
	tabuleiro1 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]
	tabuleiro2 = [['-' for x in range(largura_tabuleiro)] for y in range(altura_tabuleiro)]

preencher_navios(qtd_jogadores)
preencher_bombas(qtd_jogadores)

# Print

print('')

for line in tabuleiro1:
  print ('  '.join(map(str, line)))

print('')
print('')
print('')
print('')

for line in tabuleiro2:
  print ('  '.join(map(str, line)))
