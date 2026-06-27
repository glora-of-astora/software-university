from math import floor

w = float(input())
h = float(input())

desks_in_row = floor((h - 1) / 0.7)
desks_in_column = floor(w / 1.2)
total_desks = (desks_in_row * desks_in_column) - 3

print(floor(total_desks))