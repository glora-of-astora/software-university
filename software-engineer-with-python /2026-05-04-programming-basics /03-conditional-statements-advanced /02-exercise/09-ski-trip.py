days = int(input())
accommodation = input()
rating = input()

single_room_cost = 18.00
apartment_cost = 25.00
president_apartment_cost = 35.00
cost_before_discount = 0.0
discount = 0.0
final_cost = 0

if accommodation == 'room for one person':

    final_cost = (days - 1) * single_room_cost

elif accommodation == 'apartment':

    if days < 10:
        discount = 0.30
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50

    final_cost = ((days - 1) * apartment_cost
                  - (days - 1) * apartment_cost * discount)

elif accommodation == 'president apartment':

    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20

    final_cost = ((days - 1) * president_apartment_cost
                 - (days - 1) * president_apartment_cost * discount)

if rating == 'positive':
    final_cost += 0.25 * final_cost
elif rating == 'negative':
    final_cost -= 0.10 * final_cost

print(f'{final_cost:.2f}')