import math

avg_speed = float(input())
litres_fuel_per_100km = float(input())

distance = 384400 # km
time_spent_on_moon = 3 # hrs

hours = 2 * (distance / avg_speed) + time_spent_on_moon
fuel_needed = 2 * (distance / 100 * litres_fuel_per_100km)

print(math.ceil(hours))
print(math.ceil(fuel_needed))