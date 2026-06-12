veg_price = float(input())
fruit_price = float(input())
total_veg_in_kg = int(input())
total_fruit_in_kg = int(input())

total_order_in_bgn = ((total_veg_in_kg * veg_price)
               + (total_fruit_in_kg * fruit_price))
total_order_in_eur = total_order_in_bgn / 1.94

print(f'{total_order_in_eur:.2f}')
