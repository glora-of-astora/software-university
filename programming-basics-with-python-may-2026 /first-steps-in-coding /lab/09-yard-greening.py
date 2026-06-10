square_meters = float(input())

square_meter_price = 7.61
discount_percentage = 0.18

discount_amount = square_meters * square_meter_price * discount_percentage
final_price = square_meters * square_meter_price - discount_amount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_amount} lv.")
