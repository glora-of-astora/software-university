n = int(input())

p1 = p2 = p3 = p4 = p5 = 0.0
sum_p1 = sum_p2 = sum_p3 = sum_p4 = sum_p5 = 0
sum_all = 0

for i in range(n):
    num = int(input())

    if num < 200:
        sum_p1 += 1
    elif 200 <= num <= 399:
        sum_p2 += 1
    elif 400 <= num <= 599:
        sum_p3 += 1
    elif 600 <= num <= 799:
        sum_p4 += 1
    elif num >= 800:
        sum_p5 += 1

sum_all = sum_p1 + sum_p2 + sum_p3 + sum_p4 + sum_p5

p1 = sum_p1 / sum_all * 100
p2 = sum_p2 / sum_all * 100
p3 = sum_p3 / sum_all * 100
p4 = sum_p4 / sum_all * 100
p5 = sum_p5 / sum_all * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')