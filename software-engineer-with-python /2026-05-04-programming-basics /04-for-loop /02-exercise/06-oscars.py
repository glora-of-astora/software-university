name = input()
initial_points = float(input())
judges = int(input())

total_points = initial_points + 0

for i in range(1, judges + 1):
    judge_name = input()
    new_points = float(input())
    total_points += (len(judge_name) * new_points) / 2

    if total_points >= 1250.5:
        print(f'Congratulations, {name} got a nominee for leading role with {round(total_points, 1)}!')
        break
if total_points < 1250.5:
    print(f'Sorry, {name} you need {round((1250.5 - total_points), 1)} more!')