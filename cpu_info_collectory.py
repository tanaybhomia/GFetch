import json
import cpuinfo

def get_cpu_info():
    try:
        info = cpuinfo.get_cpu_info()
        return {"brand_raw": info["brand_raw"]}
    except Exception as e:
        print(f"Error retrieving CPU information: {e}")
        return {"brand_raw": "Unknown"}

def save_to_json(data, filename='cpu_info.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    cpu_info = get_cpu_info()
    save_to_json(cpu_info)
