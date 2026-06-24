budget = int(input())
season = input()
fishermen = int(input())

rent = 0.0
discount1 = 0.0
discount2 = 0.0

if season == 'Spring':
    rent = 3000.00
elif season == 'Summer':
    rent = 4200.00
elif season == 'Autumn':
    rent = 4200.00
elif season == 'Winter':
    rent = 2600.00

if fishermen <= 6:
    discount1 = 0.10
elif 7 < fishermen <= 11:
    discount1 = 0.15
elif fishermen > 12:
    discount1 = 0.25

if ((fishermen % 2 == 0) and not (season == 'Autumn')):
    discount2 = 0.05

cost = ((rent - rent * discount1)
        - (rent - rent * discount1) * discount2)

if budget >= cost:
    print(f'Yes! You have {budget-cost:.2f} leva left.')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva.')


