length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length * width * height) / 1000

litres_capacity = volume - ((percent / 100) * volume)

print(litres_capacity)
