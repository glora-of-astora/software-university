chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken = 10.35
fish = 12.40
vegetarian = 8.15
delivery_fee = 2.50

dessert = (((chicken_menus * chicken)
    + (fish_menus * fish) + (vegetarian_menus * vegetarian)) * 0.2)

total_order = (((chicken_menus * chicken) 
    + (fish_menus * fish) + (vegetarian_menus * vegetarian)) 
    + dessert 
    + delivery_fee)

print(total_order)
