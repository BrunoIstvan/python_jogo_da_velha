import random

JOGADOR_1 = 'Player 1'
JOGADOR_2 = 'Player 2'


def display_board(board):

    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---|---|---')
    print(f' {board[1]} | {board[2]} | {board[3]} ')


def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'{JOGADOR_1} - Escolha X ou O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    row1 = board[1] == board[2] == board[3] == mark
    row2 = board[4] == board[5] == board[6] == mark
    row3 = board[7] == board[8] == board[9] == mark
    col1 = board[1] == board[4] == board[7] == mark
    col2 = board[2] == board[5] == board[8] == mark
    col3 = board[3] == board[6] == board[9] == mark
    diag1 = board[1] == board[5] == board[9] == mark
    diag2 = board[3] == board[5] == board[7] == mark
    return row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player):

    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f'{player} - Informe uma posição (1-9): '))
    return position


def replay():
    choise = input('Jogar novamente? Informe S(Sim) ou N(Não): ').upper()
    return choise == 'S'


def choose_first():

    flip = random.randint(0, 1)
    return JOGADOR_1 if flip == 0 else JOGADOR_2


def play():

    print('Bem vindo ao Jogo-da-Velha')

    while True:

        the_board = [' ']*10
        p1, p2 = player_input()

        turn = choose_first()
        print(turn + ' vai jogar primeiro!')

        while True:

            display_board(the_board)
            position = player_choice(the_board, turn)

            if turn == JOGADOR_1:

                place_marker(the_board, p1, position)

                if win_check(the_board, p1):
                    display_board(the_board)
                    print(f'{JOGADOR_1} ganhou!!!')
                    break
                else:

                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Houve um empate')
                        break

                    else:
                        turn = JOGADOR_2

            else:

                place_marker(the_board, p2, position)

                if win_check(the_board, p2):
                    display_board(the_board)
                    print(f'{JOGADOR_2} ganhou!!!')
                    break
                else:

                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Houve um empate')
                        break

                    else:
                        turn = JOGADOR_1

        if not replay():
            break


if __name__ == '__main__':

    play()



