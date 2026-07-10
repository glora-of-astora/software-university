tabs = int(input())
salary = int(input())

penalty = 0

for i in range(tabs):
    site = input()
    
    if site == 'Facebook':
        penalty += 150
    elif site == 'Instagram':
        penalty += 100
    elif site == 'Reddit':
        penalty += 50

    if penalty >= salary:
        print('You have lost your salary.')
        break

if salary - penalty > 0:
    print(salary - penalty)