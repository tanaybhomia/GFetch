import subprocess

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

# Display the CPU model
print(f"CPU Model: {cpu_model}")