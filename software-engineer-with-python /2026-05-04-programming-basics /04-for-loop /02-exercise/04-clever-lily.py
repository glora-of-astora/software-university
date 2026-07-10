age = int(input())
machine_price = float(input())
toy_price = int(input())

even_years = 0
odd_years = 0
toys_count = 0
savings = 0.00
stolen_savings = 0.00

for i in range(1, age + 1):
    if i % 2 == 0:
        even_years += 1
        savings += 10 * even_years
    elif i % 2 == 1:
        odd_years += 1

stolen_savings = even_years
toys_count = odd_years

savings += (toys_count * toy_price) - stolen_savings

if savings >= machine_price:
    print(f'Yes! {(savings - machine_price):.2f}')
else:
    print(f'No! {abs(savings - machine_price):.2f}')