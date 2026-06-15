budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_costs_perc = int(input())

if nights > 7:
    price_per_night *= 0.95

total_costs = ((nights * price_per_night)
               + budget * (additional_costs_perc / 100))

if budget >= total_costs:
    print(f'Ivanovi will be left with {(budget - total_costs):.2f} leva after vacation.')
else:
    print(f'{abs(budget - total_costs):.2f} leva needed.')
