tabuleiro = [' ' for _ in range(9)]

def mostra_tabuleiro():
    print(tabuleiro[0] + '  | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('---|---|---')
    print(tabuleiro[3] + '  | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('---|---|---')
    print(tabuleiro[6] + '  | ' + tabuleiro[7] + ' | ' + tabuleiro[8])

def jogo():
    jogador = 'X'
    jogadas_validas = 0

    while jogadas_validas < 9:
        mostra_tabuleiro()
        print(f'Jogador {jogador}, escolha uma posição (0-8)')
        posicao = int(input())
        while posicao <0 or posicao >8:
            print(f'Posição inválida, digite um número de 0 a 8')
            posicao = int(input())

        if tabuleiro[posicao] == ' ':
            tabuleiro[posicao] = jogador
            jogadas_validas += 1
        else:
            print('posição ocupada, tente novamente')
            continue

        if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != ' ' or
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != ' ' or
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != ' ' or
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != ' ' or
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != ' ' or
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ' ' or
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ' or
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' '):
            mostra_tabuleiro()
            print(f'O jogador {jogador} venceu!')
            return
        
        jogador = 'O' if jogador == 'X' else 'X'
    mostra_tabuleiro()
    print('Empate!')

jogo()