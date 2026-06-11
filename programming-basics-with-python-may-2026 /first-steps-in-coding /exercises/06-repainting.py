nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags = 0.40

total_products = (((nylon + 2) * nylon_price) 
    + ((paint + 0.1 * paint) * paint_price) 
    + (thinner * thinner_price) 
    + bags)

repairmen_wages = total_products * hours * 0.30

total_expenses = total_products + repairmen_wages

print(total_expenses)
