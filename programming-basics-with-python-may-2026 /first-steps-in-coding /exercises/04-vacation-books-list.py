total_pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

total_hours = total_pages / pages_per_hour
hours_a_day = total_hours // total_days

print(hours_a_day)
