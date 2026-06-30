n = int(input())
result = 0

for power in range(0, n + 1):
    if power % 2 == 0:
        result = 2 ** power
        print(result)