dessert = input()
pieces = int(input())
day_of_month = int(input())

if day_of_month <= 15:
    Cake_price = 24.00
    Souffle_price = 6.66
    Baklava_price = 12.60
else:
    Cake_price = 28.70
    Souffle_price = 9.80
    Baklava_price = 16.98

if dessert == 'Cake':
    total_order = Cake_price * pieces
elif dessert == 'Souffle':
    total_order = Souffle_price * pieces
elif dessert == 'Baklava':
    total_order = Baklava_price * pieces

if day_of_month <= 22:

    if 100 <= total_order <= 200:
        total_order *= 0.85
    elif total_order > 200:
        total_order *= 0.75

    if day_of_month <= 15:
        total_order *= 0.90 # additional discount

print(f'{total_order:.2f}')