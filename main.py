
# ==========================================
# OS ResourceX
# Main Application
# ==========================================

from modules.cpu_scheduling import run_cpu_scheduling
from modules.memory_management import run_memory_management
from modules.deadlock import run_deadlock
from modules.disk_scheduling import run_disk_scheduling
from modules.analytics import run_performance_analysis
from utils.logger import log_activity, view_logs


def display_menu():
    print("\n" + "=" * 50)
    print("          WELCOME TO OS ResourceX")
    print("  Operating System Resource Management Simulator")
    print("=" * 50)

    print("\n1. CPU Scheduling Simulator")
    print("2. Memory Management Simulator")
    print("3. Deadlock Detection and Avoidance")
    print("4. Disk Scheduling Simulator")
    print("5. Performance Analysis and Comparison")
    print("6. View Activity Logs")
    print("7. Exit")

    print("=" * 50)


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice (1-7): ")
        log_activity(f"User selected menu option {choice}")

        if choice == "1":
            run_cpu_scheduling()

        elif choice == "2":
            run_memory_management()

        elif choice == "3":
            run_deadlock()

        elif choice == "4":
            run_disk_scheduling()

        elif choice == "5":
            run_performance_analysis()

        elif choice == "6":
            view_logs()

        elif choice == "7":
            log_activity("Application exited")
            print("Thank you for using OS ResourceX!")
            
            break

        else:
            print("\nInvalid choice! Enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
