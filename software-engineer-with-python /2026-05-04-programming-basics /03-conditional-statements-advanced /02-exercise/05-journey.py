budget = float(input())
season = input()
destination = ''
holiday_type = ''
holiday_cost = 0.0

if budget <= 100:
    destination = 'Bulgaria'
elif 100 < budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if season == 'summer':
    holiday_type = 'Camp'
    if destination == 'Europe':
        holiday_type = 'Hotel'
elif season == 'winter':
    holiday_type = 'Hotel'

if (destination == 'Bulgaria') and (season == 'summer'):
    holiday_cost = 0.30 * budget
elif (destination == 'Bulgaria') and (season == 'winter'):
    holiday_cost = 0.70 * budget
elif (destination == 'Balkans') and (season == 'summer'):
    holiday_cost = 0.40 * budget
elif (destination == 'Balkans') and (season == 'winter'):
    holiday_cost = 0.80 * budget
elif (destination == 'Europe') and ((season == 'summer') or (season == 'winter')):
    holiday_cost = 0.90 * budget

print(f'Somewhere in {destination}')
print(f'{holiday_type} - {holiday_cost:.2f}')