wrapping_paper = int(input())
cloth_rolls = int(input())
glue_litres = float(input())
discount_rate = int(input())

total_order = ((wrapping_paper * 5.80) + (cloth_rolls * 7.20) + (glue_litres * 1.20))
total_order -= total_order * discount_rate / 100

print(f"{total_order:.3f}")
