cinema_screening_type = input()
rows = int(input())
columns = int(input())
ticket_price = 0

if cinema_screening_type == 'Premiere':
    ticket_price = 12.00
elif cinema_screening_type == 'Normal':
    ticket_price = 7.50
elif cinema_screening_type == 'Discount':
    ticket_price = 5.00

profit = ticket_price * rows * columns
print(f'{profit:.2f} leva')