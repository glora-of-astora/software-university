animal = input()
animal_type = ''

if ((animal == 'crocodile')
    or (animal == 'snake')
    or (animal == 'tortoise')):
    animal_type = 'reptile'

elif animal ==  'dog':
    animal_type = 'mammal'

else:
    animal_type = 'unknown'

print(animal_type)