pens_pcs = int(input())
markers_pcs = int(input())
cleaner_pcs = int(input())
discount = int(input())

pens_pcs_price = 5.80
markers_pcs_price = 7.20
cleaner_pcs_price = 1.20

total_order = (pens_pcs * pens_pcs_price) + (markers_pcs * markers_pcs_price) + (cleaner_pcs * cleaner_pcs_price)

total_order_after_discount = total_order - total_order * (discount / 100)
print(total_order_after_discount)
