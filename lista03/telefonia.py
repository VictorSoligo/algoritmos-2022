resposta = input('Que horas a ligação começou: (00:00)\n')
tempo_inicial = resposta.split(':')
horas_inicial = int(tempo_inicial[0])
minutos_inicial = int(tempo_inicial[1])

inicial = horas_inicial * 60 + minutos_inicial

resposta = input('\nQue horas a ligação terminou: (00:00)\n')
tempo_final = resposta.split(':')
horas_final = int(tempo_final[0])
minutos_final = int(tempo_final[1])

final = horas_final * 60 + minutos_final

valor_minuto_ligacao = float(input('\nQuanto custa o valor por minuto de ligação:\n'))

diferenca_em_minutos = final - inicial

print(f'\nA ligação durou {diferenca_em_minutos} minutos')

desconto = 0

if (horas_inicial >= 0 and horas_inicial <= 9):
  if (horas_final >= 0 and horas_final <= 9): 
    dif = final - inicial
    print("Minutos com desconto: ", dif)
    print("Valor cobrado: ", dif * (valor_minuto_ligacao * 0.5))
  else:
    normal = final - 9 * 60
    desc = 9 * 60 - inicial
    print("Minutos com desconto", desc)
    valor_desc = desc * (valor_minuto_ligacao * 0.5)
    print("Valor com desconto", valor_desc)
    print("Valor sem desconto", normal)
    print("Total da ligação", normal + valor_desc)
elif (horas_inicial > 9 and horas_inicial <= 18):
  desconto = 0
  print('A ligação não teve desconto')
  print("Valor cobrado: ", diferenca_em_minutos * valor_minuto_ligacao)
elif (horas_inicial > 18 and horas_inicial <= 21):
  desconto = 30
  print(f'Desconto de 30%')
  print("Valor cobrado: ", diferenca_em_minutos * (valor_minuto_ligacao * 0.3))
else:
  desconto = 40
  print(f'Desconto de 30%')
  print("Valor cobrado: ", diferenca_em_minutos * (valor_minuto_ligacao * 0.4))
