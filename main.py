import os
import platform
import getpass
import psutil
from datetime import datetime, timedelta

# Get username and operating system
username = getpass.getuser()
os_type = platform.system()

# Memory information
memory_info = psutil.virtual_memory()
percent_used = memory_info.percent

# Battery information
battery_info = psutil.sensors_battery()
battery_percent = battery_info.percent
battery_status = "Charging" if battery_info.power_plugged else "Discharging"
finalbattery = "Random"

# Uptime calculation
boot_time = psutil.boot_time()
current_time = psutil.time.time()
uptime_seconds = current_time - boot_time

def format_uptime(uptime):
    days, remainder = divmod(uptime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{int(days)} days {int(hours)} hours {int(minutes)} minutes"


if (battery_percent >= 60):
    finalbattery = (f"🔋 : {battery_percent}% ({battery_status})")
else :
    finalbattery = (f"🪫 : {battery_percent}% ({battery_status})")
    
formatted_uptime = format_uptime(uptime_seconds)

# Print information
print(f"👤 : {username}")
print(f"💻 : {os_type}")
print(f"🐏 : {percent_used}%")
print(finalbattery)
print(f"⌛ : {formatted_uptime}")
