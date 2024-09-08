import time
import datetime
from rich import print  # Importing the rich library for enhanced terminal output

# Set the target date for New Year's
NY = datetime.datetime(2025, 1, 1)

# Small negative timedelta to stop the countdown precisely at zero
DELTA = datetime.timedelta(microseconds=-0.00000001)

while True:
    # Calculate the time remaining until New Year's
    time_until_ny = NY - datetime.datetime.now()
    # Get the total seconds left
    sec_left = time_until_ny.total_seconds()

    # Convert total seconds into days, hours, minutes, and seconds
    days, remainder = divmod(sec_left, 86400)  # 86400 seconds in a day
    hours, remainder = divmod(remainder, 3600)  # 3600 seconds in an hour
    minutes, seconds = divmod(remainder, 60)  # 60 seconds in a minute

    # Check if the countdown is complete
    if time_until_ny < DELTA:
        print("🎉 Happy New Year! 🎉")  # Print celebration message
        break  # Exit the loop
    else:
        # Print the countdown timer, using '\r' to overwrite the previous line
        print(f"{int(days)} Days {int(hours)} Hours {int(minutes)} Minutes {int(seconds)} Seconds", end="\r")
    
    # Wait for 1 second before the next update
    time.sleep(1)
