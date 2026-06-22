age = float(input())
sex = input()
result = ''

if sex == 'm':
    if age < 16:
        result = 'Master'
    elif age >= 16:
        result = 'Mr.'
if sex == 'f':
    if age < 16:
        result = 'Miss'
    elif age >= 16:
        result = 'Ms.'

print(result)
