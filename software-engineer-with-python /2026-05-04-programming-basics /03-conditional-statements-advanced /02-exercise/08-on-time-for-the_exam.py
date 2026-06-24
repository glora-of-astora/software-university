exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_total_minutes = (exam_hours * 60) + exam_minutes
arrival_total_minutes = (arrival_hours * 60) + arrival_minutes

difference = exam_total_minutes - arrival_total_minutes
result = ''

if 0 <= difference <= 30:
    result = 'On time'
elif difference < 0:
    result = 'Late'
elif difference > 30:
    result = 'Early'

print(result)

if difference != 0:

    if 0 < difference < 60:
        print(f'{difference} minutes before the start')
    elif -60 < difference < 0:
        print(f'{abs(difference)} minutes after the start')
    elif difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        print(f'{hours}:{minutes:02d} hours before the start')
    elif difference <= -60:
        hours = abs(difference) // 60
        minutes = abs(difference) % 60
        print(f'{hours}:{minutes:02d} hours after the start')