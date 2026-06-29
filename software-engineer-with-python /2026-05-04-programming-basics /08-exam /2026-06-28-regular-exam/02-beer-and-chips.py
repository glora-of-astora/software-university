import math

name = input()
budget = float(input())
beer_bottles = int(input())
chips_packets = int(input())

beer_price = 1.20
chips_price = 0.45 * (beer_bottles * beer_price)

total_order = (beer_bottles * beer_price) + math.ceil(chips_packets * chips_price)

if budget >= total_order:
    print(f'{name} bought a snack and has {budget - total_order:.2f} leva left.')
else:
    print(f'{name} needs {total_order - budget:.2f} more leva!')
