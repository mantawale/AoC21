def extract_board(board_set, start_line):

    output_board = []
    for i in range(start_line, start_line + 5):
        output_board.append(board_set[i].split())
    
    return output_board

def win_check(test_board):

    for row in test_board:
        if row.count('x') == 5:
            return 'bingo'

    for i in range(0, 5):
        column = []
        for row in test_board:
            column.append(row[i])
        if column.count('x') == 5:
            return 'bingo' 

    return 'nowin'

def play_board(test_board, draw_set):

    for i in draw_set:
        for k in test_board:
            if i in k:
                k[k.index(i)] = 'x'
                if win_check(test_board) == 'bingo':
                    return [i, str(draw_set.index(i))]
    
    return 'loser'

def bingo_game(game_set):
    
    draws = game_set[0].split(',')
    line = 2

    boards = []
    speeds = []
    final_calls = []

    while line <= len(game_set) - 5:
        board = extract_board(game_set, line)
        marked_board = play_board(board, draws)

        boards.append(board)
        speeds.append(marked_board[1])
        final_calls.append(marked_board[0])

        line += 6
    
    winner = [boards[speeds.index(min(speeds))], final_calls[speeds.index(min(speeds))]]
    loser = [boards[speeds.index(max(speeds))], final_calls[speeds.index(max(speeds))]]

    return [winner, loser]

def board_score(test_board):

    ending_call = int(test_board[1])
    
    ending_sum = 0
    for i in range(0, 5):
        for k in test_board[0][i]:
            if k != 'x':
                ending_sum += int(k)

    return ending_sum * ending_call

with open('day4input.txt') as input:
    squid_game = input.readlines()

squid_game_winner = bingo_game(squid_game)[0]
squid_game_loser = bingo_game(squid_game)[1]

print('Winning Score: ' + str(board_score(squid_game_winner)) + '\n' + 'Losing Score: ' + str(board_score(squid_game_loser)))
