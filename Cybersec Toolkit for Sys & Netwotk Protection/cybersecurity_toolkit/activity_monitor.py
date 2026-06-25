import psutil
from datetime import datetime

def list_running_processes():
    print("\n--- Running Processes ---")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print(proc.info)
        except:
            pass

def monitor_cpu_memory():
    print("\n--- System Usage ---")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")

def log_activity():
    with open("activity.log", "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"CPU: {psutil.cpu_percent()}%\n")
        f.write(f"Memory: {psutil.virtual_memory().percent}%\n")
