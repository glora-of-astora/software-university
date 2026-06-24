import math

racket_price = float(input())
rackets_count = int(input())
shoes_count = int(input())

shoes_price = 1/6 * racket_price
equipment1 = ((rackets_count * racket_price) + (shoes_count * shoes_price))
equipment2 = 0.2 * equipment1

total_equipment_cost = equipment1 + equipment2

print(f'Price to be paid by Djokovic {math.floor(1/8 * total_equipment_cost):.0f}')
print(f'Price to be paid by sponsors {math.ceil(7/8 * total_equipment_cost):.0f}')