# OS ResourceX
### Operating System Resource Management Simulator

## 1. Project Overview

OS ResourceX is an integrated Python-and-Bash application designed to simulate important operating system resource-management functions. It demonstrates how operating systems manage CPU processes, memory allocation, deadlocks, and disk scheduling.

The application provides an interactive menu, algorithm comparisons, performance analysis, and activity logging.

## 2. Objectives

- Understand major operating system resource-management concepts.
- Implement and simulate different OS algorithms using Python.
- Integrate Python modules with Bash scripts.
- Compare algorithm performance using common inputs.
- Maintain activity logs and handle user inputs.

## 3. Features

### CPU Scheduling
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
- Priority Scheduling

### Memory Management
- First Fit
- Best Fit
- Worst Fit
- Comparison of memory allocation algorithms

### Deadlock Management
- Banker's Algorithm
- Need matrix calculation
- Safe sequence detection

### Disk Scheduling
- FCFS
- SSTF
- SCAN
- C-SCAN

### Performance Analysis
- Algorithm comparison
- Total head movement
- Best-performing disk scheduling algorithm
- Performance improvement calculation

### Activity Logging
- Records user menu selections.
- Stores timestamps.
- Displays previously recorded activities.

## 4. Technologies Used

- Python 3
- Bash Shell Scripting
- macOS / Linux Terminal
- Visual Studio Code

No external Python libraries are required for the core application.

## 5. Project Structure

```text
OS-ResourceX/
├── main.py
├── config.py
├── modules/
│   ├── cpu_scheduling.py
│   ├── memory_management.py
│   ├── deadlock.py
│   ├── disk_scheduling.py
│   └── analytics.py
├── utils/
│   ├── input_handler.py
│   ├── logger.py
│   └── validators.py
├── data/
│   ├── sample_input.json
│   └── results/
├── scripts/
│   ├── run.sh
│   └── cleanup.sh
├── tests/
├── screenshots/
├── reports/
├── logs/
└── README.md
```

## 6. How to Run the Project

### Requirements
- Python 3 installed
- Bash shell
- macOS or Linux operating system

### Step 1: Open the project directory

```bash
cd ~/Desktop/OS-ResourceX
```

### Step 2: Give execution permission to the scripts

```bash
chmod +x scripts/run.sh
chmod +x scripts/cleanup.sh
```

### Step 3: Launch the application

```bash
./scripts/run.sh
```

Alternatively, run the Python application directly:

```bash
python3 main.py
```

### Step 4: Select an operation

Choose an option from the main menu and follow the instructions displayed on the terminal.

Enter `7` to exit the application normally.

## 7. Bash Script Integration

**run.sh:** Launches the Python application from the project directory.

**cleanup.sh:** Removes temporary Python cache directories and `.pyc` files while preserving source files and activity logs.

Execute the cleanup script using:

```bash
./scripts/cleanup.sh
```

## 8. Activity Logs

User activity is recorded in:

```text
logs/activity.log
```

The log file stores timestamps and selected menu options. Select option 6 in the application to view the activity logs.

## 9. Testing

The application is tested using valid sample inputs and integrated menu operations.

Testing areas include:
- CPU scheduling calculations
- Memory allocation strategies
- Deadlock safety detection
- Disk scheduling head movement
- Performance comparison
- Activity logging
- Bash script execution

Detailed test cases are maintained in the `tests/` directory.

## 10. Conclusion

OS ResourceX provides a practical demonstration of major operating system resource-management techniques through an integrated Python-and-Bash application.

It helps understand algorithm behaviour, resource allocation, process scheduling, deadlock avoidance, and disk performance through interactive simulations and analytical results.