import sys

new_input = input()
min_number = sys.maxsize

while new_input != 'Stop':
    new_number = int(new_input)

    if new_number < min_number:
        min_number = new_number

    new_input = input()

print(min_number)