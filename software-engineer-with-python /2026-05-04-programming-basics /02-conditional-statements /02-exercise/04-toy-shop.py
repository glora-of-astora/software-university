vacation = float(input())
puzzle_pcs = int(input())
doll_pcs = int(input())
teddy_bear_pcs = int(input())
minion_pcs = int(input())
truck_pcs = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

toys_pcs = puzzle_pcs + doll_pcs + teddy_bear_pcs + minion_pcs + truck_pcs

total_order = ((puzzle_pcs * puzzle_price)
    + (doll_pcs * doll_price)
    + (teddy_bear_pcs * teddy_bear_price)
    + (minion_pcs * minion_price)
    + (truck_pcs * truck_price))

discount = 0.25
rent = 0.1

if toys_pcs >= 50:
    profit = (total_order - discount * total_order
              - rent * (total_order - discount * total_order))

else:
    profit = (total_order - (rent * total_order))

if profit >= vacation:
    print(f"Yes! {(profit - vacation):.2f} lv left.")
else:
    print(f"Not enough money! {(vacation - profit):.2f} lv needed.")