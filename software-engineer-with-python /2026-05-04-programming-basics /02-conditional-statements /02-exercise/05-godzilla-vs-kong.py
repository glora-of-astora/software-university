budget = float(input())
extras = int(input())
clothing_price_per_extra = float(input())

decor = 0.1
discount = 0.1

expenses = ((extras * clothing_price_per_extra)
            + decor * budget)
expenses_with_discount = ((extras * clothing_price_per_extra)
                          - discount * (extras * clothing_price_per_extra)
                          + decor * budget)

if extras <= 150:
    if expenses > budget:
        print("Not enough money!")
        print(f"Wingard needs {(expenses - budget):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(budget - expenses):.2f} leva left.")

if extras > 150:
    if expenses_with_discount > budget:
        print("Not enough money!")
        print(f"Wingard needs {(expenses_with_discount - budget):.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {(budget - expenses_with_discount):.2f} leva left.")