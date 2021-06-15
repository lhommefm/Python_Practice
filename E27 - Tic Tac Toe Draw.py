def tic_tac_toe_input():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    symbol_map={ 1:'X', 2:'O' }
    player_map={ 1:2, 2:1 }

    current_player = 1
    
    while sum(x.count(0) for x in board) > 0:
        
        # get the user's move and clean up
        move = input(F'Player {current_player} ({symbol_map[current_player]}): what is your move? Use x,y coordinates where 1,1 is the top left.').strip()
        move = move.split(",")
        move = [int(x)-1 for x in move]

        # if the move is legal, update the board and switch players
        if board[move[0]][move[1]]==0:
           board[move[0]][move[1]] = current_player
           print_board[move[0]][move[1]] = symbol_map[current_player]
           current_player = player_map[current_player]
           print(board)
        
        else:
           print("That space is already taken, please try again")
           
tic_tac_toe_input()