import os
import platform
import subprocess
import shutil

def add_to_path(bin_directory):
    # Get the user's home directory
    home_directory = os.path.expanduser("~")

    # Get the current PATH variable value and split it into a list of directories
    current_path = os.environ.get("PATH", "").split(os.pathsep)

    # Check if the 'bin' directory is already in the PATH
    if bin_directory not in current_path:
        # Add the 'bin' directory to the beginning of the PATH list
        updated_path = [bin_directory] + current_path

        # Join the directories back into a string with the appropriate separator
        updated_path_str = os.pathsep.join(updated_path)

        # Update the PATH environment variable for the current session
        os.environ["PATH"] = updated_path_str

        # Save the updated PATH to the system environment variable permanently
        if platform.system() == "Windows":
            subprocess.run(["setx", "PATH", updated_path_str], shell=True)
        else:
            # For non-Windows systems, update the user's profile to add the PATH
            profile_file = os.path.join(home_directory, ".profile")
            with open(profile_file, "a") as f:
                f.write(f"\nexport PATH={updated_path_str}")

def create_expense_tracker_executable():
    # Set the script name and output directory for the Expense Tracker
    script_name = "main.py"  # This is the name of your main script
    output_directory = "dist"

    # Run PyInstaller to create the single-file executable
    cmd = f'pyinstaller --onefile {script_name} --distpath "{output_directory}" --noconfirm --log-level ERROR'
    subprocess.run(cmd, shell=True)

    # Rename the executable (remove the .exe extension on non-Windows systems)
    if platform.system() != "Windows":
        shutil.move(os.path.join(output_directory, "gfetch.exe"), os.path.join(output_directory, "main"))

def install_modules():
    required_modules = ['os', 'platform', 'getpass', 'psutil', 'subprocess', 'random']

    for module in required_modules:
        try:
            subprocess.run(['pip', 'install', module], check=True)
            print(f"Module {module} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {module}: {e}")

    # Create 'bin' directory and copy the executable to it
    bin_directory = os.path.join(os.path.expanduser("~"), "bin")
    os.makedirs(bin_directory, exist_ok=True)
    shutil.copy(os.path.join("dist", "gfetch" if platform.system() != "Windows" else "gfetch.exe"), bin_directory)

    # Add the 'bin' directory to the system's PATH
    print("Adding the Gfetch executable to the system's PATH...")
    add_to_path(bin_directory)

    print("You can now run Gfetch")

if __name__ == "__main__":
    main()
