import os
import platform
import getpass
import psutil
from datetime import datetime, timedelta
import json
from PIL import Image

# Get username and operating system
username = getpass.getuser()
os_type = platform.system()

# Memory information
memory_info = psutil.virtual_memory()
used_ram = round(memory_info.used / (1024 ** 3), 2) 
total_ram = round(memory_info.total / (1024 ** 3), 2)

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

    return f"{int(days)} days, {int(hours)} hours and {int(minutes)} minutes"


if (battery_percent >= 60):
    finalbattery = (f"🔋 : {battery_percent}% | {battery_status}")
else :
    finalbattery = (f"🪫 : {battery_percent}% | {battery_status}")
    
formatted_uptime = format_uptime(uptime_seconds)

# Processor Infromation
# Retrieve CPU information from JSON file
cpu_info_filename = 'cpu_info.json'
brandname = "Unknown"

try:
    if os.path.exists(cpu_info_filename):
        with open(cpu_info_filename, 'r') as file:
            cpu_info = json.load(file)
            brandname = cpu_info.get('brand_raw', 'Unknown')
    else:
        print(f"Error: {cpu_info_filename} does not exist.")
except Exception as e:
    print(f"Error reading CPU information from {cpu_info_filename}: {e}")

# Print information with a simple box
box_top = "+" + "-" * 50 + "+"
box_bottom = "+" + "-" * 50 + "+"

print(box_top)
print(f"|{' '*50}|")
print(f"| 👤 : {username:43} |")
print(f"| 💻 : {os_type:43} |")
print(f"| 🐏 : {used_ram} GB | {total_ram} GB  {' '*25}|")
print(f"| {finalbattery:47} |")
print(f"| ⌛ : {formatted_uptime:43} |")
print(f"| 🚀 : {brandname:43} |")
print(f"|{' '*50}|")
print(box_bottom)