control_minutes = int(input())
control_seconds = int(input())
runway_length = float(input())
seconds_per_100m = int(input())

time_correction_seconds = (runway_length / 120) * 2.5

total_control_seconds = control_minutes * 60 + control_seconds
contestant_time_seconds = seconds_per_100m / 100 * runway_length - time_correction_seconds

if contestant_time_seconds <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {contestant_time_seconds:.3f}.")
else:
    print(f"No, Marin failed! He was {(contestant_time_seconds - total_control_seconds):.3f} second slower.")