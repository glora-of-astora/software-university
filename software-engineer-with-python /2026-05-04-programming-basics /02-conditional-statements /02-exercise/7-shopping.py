budget = float(input())
gpus = int(input())
cpus = int(input())
ram_sticks = int(input())

gpu_price = 250.00
cpu_price = 0.35 * (gpus * gpu_price)
ram_stick_price = 0.10 * (gpus * gpu_price)
discount = 0.15

total_price = (gpus * gpu_price) \
    + (cpus * cpu_price) \
    + (ram_sticks * ram_stick_price)

if gpus > cpus:
    total_price -= total_price * discount

if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")