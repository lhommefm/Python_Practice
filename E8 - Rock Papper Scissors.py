def rock_paper_scissors ():
    while True:
        acceptable_answers = ['rock','paper','scissors']
        p1 = ""
        p2 = ""
        while p1 not in acceptable_answers:
            p1 = input("Player 1: what will you play? Enter 'rock', 'paper', or 'scissors")
        while p2 not in acceptable_answers:
            p2 = input("Player 2: what will you play? Enter 'rock', 'paper', or 'scissors")
        if (p1 == p2):
            print("It's a tie!")
        elif (p1 == 'rock' and p2 =='scissors') or (p1 == 'paper' and p2 =='rock') or (p1 == 'scissors' and p2 =='paper'):
            print(F'Player 1 wins with {p1} beating {p2}')
        else: 
            print(F'Player 2 wins with {p2} beating {p1}')
        restart = ""
        while restart not in ['yes', 'no']:
            restart = input("Do you want to start a new game? Enter 'yes' or 'no'")
        if restart == "yes":
            continue
        else: 
            break

rock_paper_scissors()