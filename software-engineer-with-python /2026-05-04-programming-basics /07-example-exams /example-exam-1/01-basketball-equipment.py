yearly_fee = int(input())

shoes_price = 0.6 * yearly_fee
outfit_price = 0.8 * shoes_price
ball_price = 0.25 * outfit_price
accessories_price = 0.2 * ball_price

total_cost = yearly_fee + shoes_price + outfit_price + ball_price + accessories_price

print(f'{total_cost:.2f}')
