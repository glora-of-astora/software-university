import sys

new_input = input()
max_number = -sys.maxsize

while new_input != 'Stop':
    new_number = int(new_input)

    if new_number > max_number:
        max_number = new_number

    new_input = input()

print(max_number)