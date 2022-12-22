import random
while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock paper or scissors?").lower()

    print("computer:", computer)
    print("player: " , player)

    if computer == player:
        print("tie!")
    elif player =='rock':
        if computer == 'paper':
            print('you lose')
        if computer == 'scissors':
            print('you win!')
    elif player =='scissors':
        if computer == 'rock':
            print('you lose')
        if computer == 'paper':
            print('you win!')
    elif player =='paper':
        if computer == 'scissors':
            print('you lose')
        if computer == 'rock':
            print('you win!')

    play_again =input("would you like to play again? y/n").lower()
    if play_again !='y':
        break

