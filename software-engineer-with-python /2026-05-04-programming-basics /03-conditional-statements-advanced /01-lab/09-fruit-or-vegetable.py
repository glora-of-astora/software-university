item = input()
category = ''

if ((item == 'banana')
   or (item == 'apple')
    or (item == 'kiwi')
    or (item == 'cherry')
    or (item == 'lemon')
    or (item == 'grapes')):
    category = 'fruit'
elif ((item == 'tomato')
    or (item == 'cucumber')
    or (item == 'pepper')
    or (item == 'carrot')):
    category = 'vegetable'
else:
    category = 'unknown'

print(category)