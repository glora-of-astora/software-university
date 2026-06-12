mackerel_price_per_kg = float(input())
sprinkle_price_per_kg = float(input())
bonito_kg = float(input())
saf_kg = float(input())
mussels_kg = int(input())

bonito_price_per_kg = (mackerel_price_per_kg + (mackerel_price_per_kg * 0.60))
saf_price_per_kg = (sprinkle_price_per_kg + (sprinkle_price_per_kg * 0.80))
mussels_price_per_kg = 7.50

total_order = (bonito_kg * bonito_price_per_kg) + (saf_kg * saf_price_per_kg) + (mussels_kg * mussels_price_per_kg)

print(f'{total_order:.2f}')
