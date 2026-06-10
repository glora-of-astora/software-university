dog_food = 2.50
cat_food = 4.00

dog_food_pcs = int(input())
cat_food_pcs = int(input())

dog_food_total = dog_food * dog_food_pcs
cat_food_total = cat_food * cat_food_pcs
total_order = dog_food_total + cat_food_total

print(f"{total_order} lv.")
