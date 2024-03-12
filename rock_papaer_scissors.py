#rock, paper and scissors game
import random

user_wins = 0
comp_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_ans = input('select one from rock/paper/scissors: ').lower()
    if user_ans not in options:
        continue

    comp_num = random.randint(0, 2)
    comp_ans = options[comp_num]
    max_tries = 2

    print('you choose:', user_ans)
    print('computer choose:', comp_ans)

    if user_wins < max_tries and comp_wins < max_tries:
        if user_ans == comp_ans:
            print('_' * 12)
            print('draw')
            print('_' * 12)
            continue
        elif (user_ans == 'rock' and comp_ans == 'paper') or (user_ans == 'paper' and comp_ans == 'scissors') or (user_ans == 'scissors' and comp_ans == 'rock'):
            print('_' * 12)
            print('computer wins!!')
            comp_wins += 1
            print('user wins:', user_wins)
            print('comp wins:', comp_wins)
            print('_' * 12)
            continue
        elif (user_ans == 'rock' and comp_ans == 'scissors') or (user_ans == 'paper' and comp_ans == 'rock') or (user_ans == 'scissors' and comp_ans == 'paper'):
            print('_' * 12)
            print('user wins!!')
            user_wins += 1
            print('user wins:', user_wins)
            print('comp wins:', comp_wins)
            print('_' * 12)
            continue

    else:
        if user_wins > comp_wins:
            print('you won!!')
        else:
            print('you lost!!')
        exit()