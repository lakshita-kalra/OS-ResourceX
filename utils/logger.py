
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_DIR / "logs" / "activity.log"


def log_activity(action):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {action}\n")


def view_logs():
    print("\n========== ACTIVITY LOGS ==========")

    if not LOG_FILE.exists():
        print("No activity logs found.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip():
        print(content)
    else:
        print("No activity logs found.")
