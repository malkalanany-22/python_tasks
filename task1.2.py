import time

minutes = int(input("Enter test minutes: "))
seconds = int(input("Enter test seconds: "))

TotalSeconds = (minutes * 60) + seconds

if TotalSeconds <= 0 or seconds > 59 or seconds < 0 or minutes < 0:
    print("Invalid test duration.")
    exit()

if TotalSeconds > 300:
    print("Safety limit exceeded! Test duration capped to 05:00.")
    TotalSeconds = 300

while TotalSeconds >= 0:
    mins = TotalSeconds // 60
    secs = TotalSeconds % 60
    time_format = f"{mins:02d}:{secs:02d}"
    
    if TotalSeconds > 30:
        status = f"POWER ON | Remaining: {time_format}"
    elif TotalSeconds > 10:
        status = f"STABILIZING SYSTEM | Remaining: {time_format}"
    else:
        status = f"COOLDOWN PHASE | Do not touch | {time_format}"
        
    print(status, end="\r", flush=True)
    time.sleep(1)
    TotalSeconds -= 1

print("\nPower test completed successfully.")