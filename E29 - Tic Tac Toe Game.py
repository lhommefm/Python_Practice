def tic_tac_toe_game():
    
    # define parameters
    symbol_map={ 1:'X', 2:'O' }
    player_map={ 1:2, 2:1 }

    # set state of the game
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = 1
    game_over = False

    # helper function to print the game board
    def print_game_board():
        times = len(print_board)
        count = 0
        def print_horizontal_line(times):
            line = " ---" * times
            print(line)
        def print_vertical_line():
            line = F"| {print_board[count][0]} | {print_board[count][1]} | {print_board[count][2]} |"
            print(line)
        print('Current game board:')
        while count < times:
            print_horizontal_line(times)
            print_vertical_line()
            count = count+1
        print_horizontal_line(times)

    # helper function to process inputs
    def tic_tac_toe_input():
        move = input(F'Player {current_player} ({symbol_map[current_player]}): what is your move? Use x,y coordinates where 1,1 is the top left.').strip()
        # if the move is legal, update the board and switch players
        try:
            move = move.split(",")
            move = [int(x)-1 for x in move]
            if board[move[0]][move[1]]==0:
                board[move[0]][move[1]] = current_player
                print_board[move[0]][move[1]] = symbol_map[current_player]
                print('Move accepted')
                return 1            
            else:
                print("That space is already taken, please try again")
                return 0
        except:
            print('Invalid input, please try again')
            return 0
        

    # helper function to check winnner
    def check_winner():
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
        # return result
        return winner

    # loop through making moves until the game is over
    while game_over == False:
        print_game_board()
        result = tic_tac_toe_input()
        if result != 0:
            # check game over conditions
            winner = check_winner()
            if winner != 0:
                print_game_board()
                print(F'Player {winner} Wins!')
                game_over = True
            elif sum(x.count(0) for x in board) == 0:
                print_game_board()
                print('There game is a tie!')
                game_over = True
            # continue game
            else:
                current_player = player_map[current_player]
                print(F"Player {current_player}'s turn")


tic_tac_toe_game()