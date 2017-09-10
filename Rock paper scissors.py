import random, time

ART = {'rock':'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \\ / __| |/ /
| | | (_) | (__|   < 
|_|  \\___/ \\___|_|\\_\\
                     
''','paper':'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \\ / _` | '_ \\ / _ \\ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \\__,_| .__/ \\___|_|   
| |         | |              
|_|         |_|  

''','scissors':'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \\| '__/ __|
\\__ \\ (__| \\__ \\__ \\ (_) | |  \\__ \\
|___/\\___|_|___/___/\\___/|_|  |___/

'''}

choices = ['r','p','s']

playerScore = 0
computerScore = 0
finish = False
draws = 0

def Go(choice):
    global playerScore, computerScore, draws
    if choice == 'rock':
        choice = 'r'
    elif choice == 'paper':
        choice = 'p'
    elif choice == 'scissors':
        choice = 's'
    computerChoice = random.choice(choices)
    if choice == 'r' and computerChoice == 'r':
        winner = 'draw'
    elif choice == 'r' and computerChoice == 'p':
        winner = 'computer'
    elif choice == 'r' and computerChoice == 's':
        winner = 'player'
    elif choice == 'p' and computerChoice == 'r':
        winner = 'player'
    elif choice == 'p' and computerChoice == 'p':
        winner = 'draw'
    elif choice == 'p' and computerChoice == 's':
        winner = 'computer'
    elif choice == 's' and computerChoice == 'r':
        winner = 'computer'
    elif choice == 's' and computerChoice == 'p':
        winner = 'player'
    elif choice == 's' and computerChoice == 's':
        winner = 'draw'
    else:
        raise Exception ('Sorry but I\'m not quite sure what happened here. Please try running the program again')
    if winner == 'player':
        playerScore += 1
        winner = 'you'
    elif winner == 'computer':
        computerScore += 1
        winner = 'the computer'
    elif winner == 'draw':
        draws += 1
    else:
        raise Exception('Sorry but I\'m not quite sure what happened here. Please try running the program again')
    time.sleep(1)
    print(ART['rock'])
    time.sleep(1)
    print(ART['paper'])
    time.sleep(1)
    print(ART['scissors'])
    time.sleep(1)
    print('\n\n\t',choice,' - ',computerChoice)
    return winner


def main():
    global finish
    print('Welcome to')
    time.sleep(1.5)
    print(ART['rock'])
    time.sleep(1.5)
    print(ART['paper'])
    time.sleep(1.5)
    print(ART['scissors'])
    input('Press ENTER to start')
    print('\n\nYou are playing first to 5\n\nEach round you make a selection by choosing one of:\n\n\t- rock\t\t(r)\n\t- paper\t\t(p)\n\t- scissors\t(s)\n\nYou will see the total score after each go.\n\nGood luck!')

    while not finish:
        choice = input('\n\nPlease make a selection \t').lower()
        if choice == 'r' or choice == 'p' or choice == 's' or choice == 'rock' or choice == 'paper' or choice == 'scissors':
            winner = Go(choice)
            if winner == 'you' or winner == 'the computer':
                print('\n\nThe winner of that go was ',winner,'\n\nThe score is\n\n\tYou\t',playerScore,' - ',computerScore,'\tComputer')
            elif winner == 'draw':
                print('\n\nThat was a draw, please go again\n\nThe score is\n\n\tYou\t', playerScore, ' - ',computerScore, '\tComputer')
        else:
            print('Invalid Selection\nPlease try again\n')
            pass
        if computerScore == 5:
            finish = True
        if playerScore == 5:
            finish = True
    if computerScore == 5:
        print('\nYou lost :(\nBetter luck next time\nThe final score is\n\tYou\t',playerScore,' - ',computerScore,'\tComputer')
    if playerScore == 5:
        print('Well done!\nYou won\n\nThe final score is\n\tYou\t',playerScore,' - ',computerScore,'\tComputer')


main()