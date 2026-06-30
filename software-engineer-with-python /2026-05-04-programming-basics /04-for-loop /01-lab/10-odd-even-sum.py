n = int(input())
even_sum = 0
odd_sum = 0

for inx in range(n):
    new_number = int(input())

    if inx % 2 == 0:
        even_sum += new_number

    elif inx % 2 == 1:
        odd_sum += new_number

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')