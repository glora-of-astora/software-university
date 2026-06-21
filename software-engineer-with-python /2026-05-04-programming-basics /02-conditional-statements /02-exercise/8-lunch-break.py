import math

tv_series = input()
episode_length = int(input())
lunch_break = int(input())

lunch_time = 1/8 * lunch_break
rest_time  = 2/8 * lunch_break
free_time = 5/8 * lunch_break - episode_length

if episode_length <= 5/8 * lunch_break:
    print(f"You have enough time to watch {tv_series} and left with {math.ceil(free_time)} minutes free time.")

else:
    print(f"You don't have enough time to watch {tv_series}, you need {math.ceil(episode_length - 5/8 * lunch_break)} more minutes.")