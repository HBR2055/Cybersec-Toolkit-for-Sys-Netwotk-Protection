from activity_monitor import list_running_processes, monitor_cpu_memory, log_activity
from port_scanner import scan_ports
from password_analyzer import check_strength, check_common_patterns
from utils import banner

while True:
    banner()
    choice = input("Enter choice: ")

    if choice == "1":
        print("\n1. View Running Processes")
        print("2. Check CPU/Memory Usage")
        print("3. Log Activity")

        sub = input("Choose: ")

        if sub == "1":
            list_running_processes()
        elif sub == "2":
            monitor_cpu_memory()
        elif sub == "3":
            log_activity()
            print("Activity logged.")

    elif choice == "2":
        target = input("Enter target IP (e.g., 127.0.0.1): ")
        start = int(input("Start port: "))
        end = int(input("End port: "))
        scan_ports(target, start, end)

    elif choice == "3":
        password = input("Enter password: ")
        print("Strength:", check_strength(password))
        print(check_common_patterns(password))

    elif choice == "4":
        break

    else:
        print("Invalid choice")
