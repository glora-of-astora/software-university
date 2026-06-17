people = int(input())
season = input()

cost = 0.0

if season == 'spring':
    if people > 5:
        cost = 48.00
    else:
        cost = 50.00

elif season == 'summer':
    if people > 5:
        cost = 45.00 * 0.85
    else:
        cost = 48.50 * 0.85

elif season == 'autumn':
    if people > 5:
        cost = 49.50
    else:
        cost = 60.00

elif season == 'winter':
    if people > 5:
        cost = 85.00 * 1.08
    else:
        cost = 86.00 * 1.08

total_cost = cost * people
print(f'{total_cost:.2f} leva.')
