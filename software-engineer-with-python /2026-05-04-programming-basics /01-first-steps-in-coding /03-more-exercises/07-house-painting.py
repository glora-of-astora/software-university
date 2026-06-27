x = float(input())
y = float(input())
h = float(input())

house_front_area = x ** 2 - 1.2 * 2
house_back_area = x ** 2
house_side_area = x * y - 1.5 ** 2
house_roof_area = 2 * (x * y) + 2 * ((x * h) / 2)

# green paint => 1 liter per 3.4 squared meters
# red paint => 1 liter per 4.3 squared meters

green_paint = (house_front_area + house_back_area + 2 * house_side_area) / 3.4
red_paint = house_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')