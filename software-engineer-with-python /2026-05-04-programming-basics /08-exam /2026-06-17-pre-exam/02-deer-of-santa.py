import math

days = int(input())
total_food_kg = int(input())
food_per_day_1 = float(input())
food_per_day_2 = float(input())
food_per_day_3 = float(input())

food_needed = (food_per_day_1 + food_per_day_2 + food_per_day_3) * days

if total_food_kg > food_needed:
    print(f'{math.floor(total_food_kg - food_needed):.0f} kilos of food left.')
else:
    print(f'{math.ceil(abs(total_food_kg - food_needed)):.0f} more kilos of food are needed.')
