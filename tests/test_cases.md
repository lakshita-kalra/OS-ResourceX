
# OS ResourceX - Test Cases

## 1. CPU Scheduling

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Run FCFS with valid processes | Correct completion, waiting and turnaround times |
| TC02 | Run SJF with valid processes | Processes execute in shortest-job order |
| TC03 | Run Round Robin with valid quantum | Processes execute using time quantum |
| TC04 | Enter invalid process count | Error message or safe termination |

## 2. Memory Management

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC05 | Run First Fit | Processes allocated to first suitable blocks |
| TC06 | Run Best Fit | Processes allocated to smallest suitable blocks |
| TC07 | Run Worst Fit | Processes allocated to largest suitable blocks |
| TC08 | Compare all algorithms | Allocation and utilization results displayed |

## 3. Deadlock Detection

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC09 | Run Banker’s Algorithm with safe sample | Safe sequence displayed |
| TC10 | Run Banker’s Algorithm with unsafe sample | Unsafe state reported |
| TC11 | Enter invalid matrix values | Error message displayed |

## 4. Disk Scheduling

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC12 | Run FCFS, SSTF, SCAN and C-SCAN | All algorithms display head movement |
| TC13 | Enter request outside disk boundaries | Invalid request error |
| TC14 | Compare algorithms using same input | Correct performance comparison |

## 5. Performance Analysis

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC15 | Compare disk scheduling algorithms | Ranking and best algorithm displayed |
| TC16 | Calculate improvement over FCFS | Percentage improvement displayed |

## 6. Activity Logs and Bash

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC17 | Select menu options | Activities recorded with timestamps |
| TC18 | View activity logs | Saved logs displayed |
| TC19 | Execute scripts/run.sh | Main application launches |
| TC20 | Execute scripts/cleanup.sh | Temporary Python cache files removed |
