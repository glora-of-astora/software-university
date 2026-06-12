from math import floor

w = float(input()) # in meters
h = float(input()) # in meters

desks_in_row = floor((h - 1) / 0.7)
desks_in_column = floor(w / 1.2)
total_desks = (desks_in_row * desks_in_column) - 3

if 3 <= h <= w <= 100:
    print(floor(total_desks))
