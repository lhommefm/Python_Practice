def print_horizontal_line(times):
    line = " ---" * times
    print(line)

def print_vertical_line(times):
    line = "|   " * times + "|"
    print(line)

def print_game_board():
    times = int(input("How many squares per side of the board?"))
    count = 0
    while count < times:
        print_horizontal_line(times)
        print_vertical_line(times)
        count = count+1
    print_horizontal_line(times)

print_game_board()