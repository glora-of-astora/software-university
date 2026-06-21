points = int(input())
bonus = 0
extra_bonus = 0

if points <= 100:
    bonus = 5
elif 100 < points <= 1000:
    bonus = points * 0.2
elif points > 1000:
    bonus = points * 0.1

if points % 2 == 0:
    extra_bonus = 1

if points % 5 == 0: # A BETTER WAY IS "if points % 10 == 5"
    if points % 2 != 0:
        extra_bonus = 2

print(bonus + extra_bonus)
print(bonus + extra_bonus + points)

