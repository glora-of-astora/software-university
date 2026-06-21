current_record = float(input()) # IN SECONDS
meters = float(input()) # TOTAL DISTANCE
seconds = float(input()) # SECONDS PER METER

water_resist = 12.5 # SECONDS DELAY PER 15 METERS

ideal_time = meters * seconds
delay = (meters // 15) * water_resist
real_time = ideal_time + delay

if real_time < current_record:
    print(f"Yes, he succeeded! The new world record is {real_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(current_record - real_time):.2f} seconds slower.")