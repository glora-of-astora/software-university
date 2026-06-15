strawberries_price_per_kg = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price_per_kg = 0.5 * strawberries_price_per_kg
oranges_price_per_kg = 0.6 * raspberries_price_per_kg
bananas_price_per_kg = 0.2 * raspberries_price_per_kg

total_order = ((strawberries_kg * strawberries_price_per_kg)
               + (bananas_kg * bananas_price_per_kg)
               + (oranges_kg *oranges_price_per_kg)
               + (raspberries_kg * raspberries_price_per_kg))

print(f'{total_order:.2f}')
