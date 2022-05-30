esta_rodando = False
produto_escolhido = False

produtos = {
    1: 'Refrigerante de cola',
    2: 'Batata frita',
    3: 'Barra de cereal',
    4: 'Água',
    5: 'Água com gás',
    6: 'Achocolatado',
    7: 'Bala de menta',
}

resposta = input('Digite INICIAR para ligar a máquina:\n')

if resposta == 'INICIAR':
    esta_rodando = True
else:
    print('\nOPERAÇÃO INVÁLIDA')

while esta_rodando != False:
    print('\nProdutos disponíveis:\n')

    for key, value in produtos.items():
        print(f'{key} - {value}')

    while produto_escolhido == False:
        produto = int(input('\nDigite o número do produto desejado:\n'))

        if (produto >= 1 and produto <= 7):
            print(f'\nProduto escolhido: {produtos.get(produto)}')
            resposta = input(
                'Digite CONFIRMAR para finalizar a operação ou CANCELAR para escolher outro produto:\n')

            if (resposta == 'CONFIRMAR'):
                print(f'\nProduto {produtos.get(produto)} será entregue')
                produto_escolhido = True
                esta_rodando = False
            elif (resposta == 'CANCELAR'):
                produto_escolhido = False
            else:
                print('\nOPERAÇÃO INVÁLIDA')
                produto_escolhido = True
                esta_rodando = False
        else:
            print('\nOPERAÇÃO INVÁLIDA')
            produto_escolhido = True
            esta_rodando = False
