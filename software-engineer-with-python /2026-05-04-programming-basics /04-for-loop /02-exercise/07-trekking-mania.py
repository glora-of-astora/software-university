num_groups = int(input())
group1 = group2 = group3 = group4 = group5 = 0
p1 = p2 = p3 = p4 = p5 = 0.0
all_group_members = 0

for i in range(1, num_groups + 1):
    group_members = int(input())

    if group_members <= 5:
        group1 += group_members
    elif 6 <= group_members <= 12:
        group2 += group_members
    elif 13 <= group_members <= 25:
        group3 += group_members
    elif 26 <= group_members <= 40:
        group4 += group_members
    elif group_members >= 41:
        group5 += group_members

all_group_members = group1 + group2 + group3 + group4 + group5

p1 = group1 / all_group_members * 100
p2 = group2 / all_group_members * 100
p3 = group3 / all_group_members * 100
p4 = group4 / all_group_members * 100
p5 = group5 / all_group_members * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')