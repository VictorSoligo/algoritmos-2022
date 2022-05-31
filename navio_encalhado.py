quantidade_areia = 0
quantidade_rebocadores = 0
quantidade_areia_suficiente = False
quantidade_rebocadores_suficiente = False
navio_encalhado = True

while navio_encalhado == True:
    while quantidade_areia_suficiente == False:
        resposta = input('Você deseja retirar mais 10 metros de areia?\n')

        if(resposta == 's'):
            quantidade_areia += 10
        elif(resposta == 'n'):
            quantidade_areia_suficiente = True
            break

    while quantidade_rebocadores_suficiente == False:
        resposta = input('Você deseja trazer mais um rebocador?\n')

        if(resposta == 's'):
            quantidade_rebocadores += 1
        elif (resposta == 'n'):
            quantidade_rebocadores_suficiente = True
            break

        resposta = input('O navio foi desencalhado?\n')

        if(resposta == 's'):
            navio_encalhado = False
            break
        elif (resposta == 'n'):
            quantidade_areia_suficiente = False
            quantidade_rebocadores_suficiente = False

print('\nO navio foi desencalhado!')
print('Quantidade de areia retirada:', quantidade_areia, "metros")
print('Quantidade de rebocadores utilizados:', quantidade_rebocadores)
print('Parabéns Equipe o navio foi desencalhado!')
