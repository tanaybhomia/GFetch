import os
import platform
import getpass
import psutil
import subprocess
import random

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

# Uptime calculation
boot_time = psutil.boot_time()
current_time = psutil.time.time()
uptime_seconds = current_time - boot_time

def format_uptime(uptime):
    days, remainder = divmod(uptime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{int(days)} days, {int(hours)} hours, and {int(minutes)} minutes"

if battery_percent >= 60:
    finalbattery = f"🔋 :: {battery_percent}% | {battery_status}"
else:
    finalbattery = f"🪫 :: {battery_percent}% | {battery_status}"

formatted_uptime = format_uptime(uptime_seconds)

# Processor Information
def get_cpu_model():
    try:
        result = subprocess.check_output(["wmic", "cpu", "get", "name"]).decode("utf-8")
        lines = result.splitlines()
        if len(lines) > 2:
            # Skip the header and get the model name
            return " ".join(lines[2:])
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving CPU information: {e}")

    return "Unknown"

# Get CPU model information
cpu_model = get_cpu_model()

# Colors for ANSI escape codes
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

# Randomly select a color for the bars
bar_color = random.choice(colors)

# Print information with a simple box
box_top = f"{bar_color}+" + "-" * 60 + "+\033[0m"
box_bottom = f"{bar_color}+" + "-" * 60 + "+\033[0m"

print(box_top)
print(f"{bar_color}|{' '*60}|\033[0m")
print(f"{bar_color}| 👤 :: {username:52} |\033[0m")
print(f"{bar_color}| 💻 :: {os_type:52} |\033[0m")
print(f"{bar_color}| 🐏 :: {used_ram:.2f} GB | {total_ram:.2f} GB  {' '*33}|\033[0m")
print(f"{bar_color}| {finalbattery:57} |\033[0m")
print(f"{bar_color}| 🚀 :: {cpu_model:52} |\033[0m")
print(f"{bar_color}| ⌛ :: {formatted_uptime:52} |\033[0m")
print(f"{bar_color}|{' '*60}|\033[0m")
print(box_bottom)
print("\n")