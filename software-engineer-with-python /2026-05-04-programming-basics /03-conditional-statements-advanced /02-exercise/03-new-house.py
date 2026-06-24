flower_type = input()
flower_pcs = int(input())
budget = int(input())
price = 0.0
discount = 0.0
price_increase = 0.0

# roses_price = 5.00
# dahlias_price = 3.80
# tulips_price = 2.80
# narcissus_price = 3.00
# gladiolus_price = 2.50

if flower_type == 'Roses':
    price = 5.00
    if flower_pcs > 80:
        discount = 0.10
elif flower_type == 'Dahlias':
    price = 3.80
    if flower_pcs > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    price = 2.80
    if flower_pcs > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    price = 3.00
    if flower_pcs < 120:
        price_increase = 0.15
elif flower_type == 'Gladiolus':
    price = 2.50
    if flower_pcs < 80:
        price_increase = 0.20

total_order = ((price * flower_pcs)
    - (price * flower_pcs * discount)
    + (price * flower_pcs * price_increase))

if total_order <= budget:
    print(f'Hey, you have a great garden with {flower_pcs} {flower_type} and {(budget - total_order):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_order - budget):.2f} leva more.')