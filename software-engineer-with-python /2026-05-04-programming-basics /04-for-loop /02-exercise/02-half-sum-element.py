import sys

n = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for i in range(n):
    new_number = int(input())
    sum_numbers += new_number

    if new_number > max_number:
        max_number = new_number

if sum_numbers - max_number == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - (sum_numbers - max_number))}')