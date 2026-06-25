first_match_score = input()
second_match_score = input()
third_match_score = input()

score1 = int(first_match_score[0])
score2 = int(first_match_score[2])
score3 = int(second_match_score[0])
score4 = int(second_match_score[2])
score5 = int(third_match_score[0])
score6 = int(third_match_score[2])

games_won = 0
games_lost = 0
drawn_games = 0

if score1 > score2:
    games_won += 1
elif score1 < score2:
    games_lost += 1
elif score1 == score2:
    drawn_games += 1

if score3 > score4:
    games_won += 1
elif score3 < score4:
    games_lost += 1
elif score3 == score4:
    drawn_games += 1

if score5 > score6:
    games_won += 1
elif score5 < score6:
    games_lost += 1
elif score5 == score6:
    drawn_games += 1

print(f'Team won {games_won} games.')
print(f'Team lost {games_lost} games.')
print(f'Drawn games: {drawn_games}')