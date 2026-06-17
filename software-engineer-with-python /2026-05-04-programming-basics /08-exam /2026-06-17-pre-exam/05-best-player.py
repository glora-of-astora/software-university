import sys

command = input()

best_player_name = ''
best_player_goals = -sys.maxsize
has_made_hat_trick = False

while command != 'END':
    name = command
    goals = int(input())

    if goals > best_player_goals:
        best_player_name = name
        best_player_goals = goals

        if goals >= 3:
            has_made_hat_trick = True

    if goals >= 10:
        break

    command = input()

print(f'{best_player_name} is the best player!')

if has_made_hat_trick:
    print(f'He has scored {best_player_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player_goals} goals.')
