month = input()
nights = int(input())

apt_price_per_night = 0.0
studio_price_per_night = 0.0
apt_discount = 0.0
studio_discount = 0.0

if (month == 'May') or (month == 'October'):
    apt_price_per_night = 65.00
    studio_price_per_night = 50.00
    if nights > 14:
        studio_discount = 0.30
        apt_discount = 0.10
    elif nights > 7:
        studio_discount = 0.05

elif (month == 'June') or (month == 'September'):
    apt_price_per_night = 68.70
    studio_price_per_night = 75.20
    if nights > 14:
        studio_discount = 0.20
        apt_discount = 0.10

elif (month == 'July') or (month == 'August'):
    apt_price_per_night = 77.00
    studio_price_per_night = 76.00
    if nights > 14:
        apt_discount = 0.10

apt_total_price = (apt_price_per_night * nights
                   - apt_price_per_night * nights * apt_discount)
studio_total_price = (studio_price_per_night * nights
                      - studio_price_per_night * nights * studio_discount)

print(f'Apartment: {apt_total_price:.2f} lv.')
print(f'Studio: {studio_total_price:.2f} lv.')