# Manually "Set" the clock
import time
print("--- Manually Set Your Clock ---")
hour = int(input("Enter current hour (0-23): "))
minute = int(input("Enter current minute (0-59): "))
second = int(input("Enter current second (0-59): "))

print("\nClock Started! Press Ctrl+C to stop.\n")

# The time Loop
while True:
    # :02d keeps it looking like 09:05:01 instead of 9:5:1
    print(f"Current Time: {hour:02d}:{minute:02d}:{second:02d}", end="\r")
    #wait exactly 1 second
    time.sleep(1)
    # Update the seconds
    second += 1
    # The "Carry Over" Logic
    if second==60:
        second=0
        minute+=1
    if minute==60:
        minute=0
        hour+=1
