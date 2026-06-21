hours = int(input())
minutes = int(input())

if minutes >= 45:
    minutes = (minutes + 15) - 60
    hours = hours + 1
else:
    minutes = minutes + 15

if hours == 24:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")

# ALTERNATIVE SOLUTION

# hours = int(input())
# minutes = int(input())
#
# if hours <= 23 and 0 <= minutes <= 44:
#     print(f"{hours}:{minutes+15}")
#
# elif hours < 23 and 45 <= minutes <= 54:
#     print(f"{hours+1}:0{minutes-45}")
#
# elif hours < 23 and 55 <= minutes <= 59:
#     print(f"{hours+1}:{minutes-45}")
#
# elif hours == 23 and 45 <= minutes <= 54:
#     print(f"0:0{minutes-45}")
#
# elif hours == 23 and 55 <= minutes <= 59:
#     print(f"0:{minutes-45}")