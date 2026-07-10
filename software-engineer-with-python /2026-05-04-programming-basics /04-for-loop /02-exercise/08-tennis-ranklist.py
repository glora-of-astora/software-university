tournaments = int(input())
initial_points = int(input())
total_points = initial_points + 0
won_tournaments = 0

for i in range(1, tournaments + 1):
    finishing_round = input()

    if finishing_round == 'W':
        total_points += 2000
        won_tournaments += 1
    elif finishing_round == 'F':
        total_points += 1200
    elif finishing_round == 'SF':
        total_points += 720

print(f'Final points: {total_points}')
print(f'Average points: {int((total_points - initial_points) / tournaments)}')
print(f'{(won_tournaments / tournaments * 100):.2f}%')