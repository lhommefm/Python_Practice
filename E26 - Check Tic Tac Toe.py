board = [[0, 0, 0], [2, 1, 0], [2, 1, 1]] 

def check_winner(board):

    winner = 0

    # check horizontal wins
    horiz_check = [horiz[0] for horiz in board if horiz[0]==horiz[1]==horiz[2]]
    if len(horiz_check)>0:
        winner = horiz_check[0]    

    # check vertical wins
    for idx, val in enumerate(board[0]):
        if board[0][idx]==board[1][idx]==board[2][idx]:
            winner = val    

    # check diagonal wins
    if board[0][0]==board[1][1]==board[2][2]:
        winner = board[1][1]
    if board[0][2]==board[1][1]==board[2][0]:
        winner = board[1][1]

    return winner

check_winner(board)