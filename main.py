import os
import platform
import getpass
import psutil
from datetime import datetime, timedelta
import json
import subprocess

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
def get_cpu_model():
    try:
        result = subprocess.check_output(["wmic", "cpu", "get", "name"]).decode("utf-8")
        lines = result.splitlines()
        if len(lines) > 2:
            # Skip the header and get the model name
            return " ".join(lines[2:])
    except subprocess.CalledProcessError:
        pass

    return "Unknown"

# Get CPU model information
cpu_model = get_cpu_model()

# Print information with a simple box
box_top = "+" + "-" * 60 + "+"
box_bottom = "+" + "-" * 60 + "+"

print(box_top)
print(f"|{' '*60}|")
print(f"| 👤 : {username:53} |")
print(f"| 💻 : {os_type:53} |")
print(f"| 🐏 : {used_ram} GB | {total_ram} GB  {' '*35}|")
print(f"| {finalbattery:57} |")
print(f"| ⌛ : {formatted_uptime:53} |")
print(f"| 🚀 : {cpu_model:53} |")
print(f"|{' '*60}|")
print(box_bottom)