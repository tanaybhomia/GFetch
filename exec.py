import os
import subprocess
import shutil

def install_required_modules():
    # List of required modules
    required_modules = ['psutil', 'cpuinfo']  # Add other required modules

    print("Installing required modules...")

    for module in required_modules:
        subprocess.run(f'pip install {module} --quiet', shell=True)

    print("Modules installed successfully.")

def make_main_executable(output_name='my_program'):
    script_name = 'main.py'  # Replace with your main script name
    bin_directory = os.path.join(os.path.expanduser("~"), "bin")
    
    # Ensure 'bin' directory exists
    os.makedirs(bin_directory, exist_ok=True)

    # Run PyInstaller to create the single-file executable with a custom name
    subprocess.run(f'pyinstaller --onefile --distpath "{bin_directory}" --name {output_name} {script_name} --noconfirm --log-level ERROR', shell=True)

    print(f"{script_name} converted to an executable named {output_name} and placed in {bin_directory}")

def execute_cpu_info_collector(output_name='my_program'):
    cpu_info_script = 'cpu_info_collector.py'  # Replace with your CPU info script name
    bin_directory = os.path.join(os.path.expanduser("~"), "bin")
    
    # Ensure 'bin' directory exists
    os.makedirs(bin_directory, exist_ok=True)

    # Run the CPU info collector script
    subprocess.run(f'python {cpu_info_script}', shell=True)

    # Move the generated JSON file to the 'bin' directory
    cpu_info_json = 'cpu_info.json'
    if os.path.exists(cpu_info_json):
        shutil.move(cpu_info_json, os.path.join(bin_directory, cpu_info_json))
        print(f"{cpu_info_json} moved to {bin_directory}")

if __name__ == '__main__':
    print("Installing and configuring the program...")

    # Install required modules
    install_required_modules()

    # Make main.py executable with a custom name and place it in the 'bin' directory
    make_main_executable(output_name='my_program')

    # Execute cpu_info_collector.py and move the generated JSON file to 'bin'
    execute_cpu_info_collector(output_name='my_program')

    print("Installation complete.")
