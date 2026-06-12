temp = float(input())

if 26.0 <= temp <= 35.0:
    print('Hot')
elif 20.1 <= temp <= 25.9:
    print('Warm')
elif 15.0 <= temp <= 20.0:
    print('Mild')
elif 12.0 <= temp <= 14.9:
    print('Cool')
elif 5.0 <= temp <= 11.9:
    print('Cold')
else:
    print('unknown')
