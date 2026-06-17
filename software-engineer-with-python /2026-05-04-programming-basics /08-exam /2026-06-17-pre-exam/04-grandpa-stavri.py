days = int(input())

total_litres = 0.0
total_abv_per_litre = 0.0

for day in range(days):
    rakiya = float(input())
    abv_per_litre = float(input())

    total_litres += rakiya
    total_abv_per_litre += abv_per_litre * rakiya

avg_abv_per_litre = total_abv_per_litre / total_litres

print(f'Liter: {total_litres:.2f}')
print(f'Degrees: {avg_abv_per_litre:.2f}')

if avg_abv_per_litre < 38:
    print(f'Not good, you should baking!')
elif 38 <= avg_abv_per_litre <= 42:
    print('Super!')
else:
    print(f'Dilution with distilled water!')
