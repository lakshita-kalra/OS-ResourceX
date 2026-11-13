
# ==============================================
# OS ResourceX - CPU Scheduling Module
# Algorithms: FCFS, SJF, Round Robin, Priority
# ==============================================

def calculate_metrics(processes, gantt):
    completion = {}

    for pid, start, end in gantt:
        completion[pid] = end

    results = []

    for p in processes:
        pid = p["pid"]
        at = p["arrival"]
        bt = p["burst"]

        ct = completion[pid]
        tat = ct - at
        wt = tat - bt
        rt = wt

        results.append({
            "pid": pid,
            "arrival": at,
            "burst": bt,
            "completion": ct,
            "turnaround": tat,
            "waiting": wt,
            "response": rt
        })

    return results


def fcfs(processes):
    ordered = sorted(processes, key=lambda p: (p["arrival"], p["pid"]))
    gantt = []
    current_time = 0

    for p in ordered:
        start = max(current_time, p["arrival"])
        end = start + p["burst"]

        gantt.append((p["pid"], start, end))
        current_time = end

    return calculate_metrics(processes, gantt), gantt


def sjf(processes):
    remaining = processes.copy()
    gantt = []
    current_time = 0

    while remaining:
        available = [
            p for p in remaining
            if p["arrival"] <= current_time
        ]

        if not available:
            current_time = min(p["arrival"] for p in remaining)
            continue

        selected = min(
            available,
            key=lambda p: (p["burst"], p["arrival"], p["pid"])
        )

        start = current_time
        end = start + selected["burst"]

        gantt.append((selected["pid"], start, end))
        current_time = end
        remaining.remove(selected)

    return calculate_metrics(processes, gantt), gantt


def round_robin(processes, quantum):
    ordered = sorted(processes, key=lambda p: (p["arrival"], p["pid"]))
    remaining = {p["pid"]: p["burst"] for p in processes}

    gantt = []
    ready_queue = []
    current_time = 0
    index = 0

    while index < len(ordered) or ready_queue:

        if not ready_queue:
            current_time = max(current_time, ordered[index]["arrival"])

        while (index < len(ordered) and
               ordered[index]["arrival"] <= current_time):
            ready_queue.append(ordered[index])
            index += 1

        p = ready_queue.pop(0)
        pid = p["pid"]

        start = current_time
        execution = min(quantum, remaining[pid])
        current_time += execution
        remaining[pid] -= execution

        gantt.append((pid, start, current_time))

        while (index < len(ordered) and
               ordered[index]["arrival"] <= current_time):
            ready_queue.append(ordered[index])
            index += 1

        if remaining[pid] > 0:
            ready_queue.append(p)

    return calculate_metrics(processes, gantt), gantt


def priority_scheduling(processes):
    remaining = processes.copy()
    gantt = []
    current_time = 0

    while remaining:
        available = [
            p for p in remaining
            if p["arrival"] <= current_time
        ]

        if not available:
            current_time = min(p["arrival"] for p in remaining)
            continue

        # Lower priority number means higher priority
        selected = min(
            available,
            key=lambda p: (p["priority"], p["arrival"], p["pid"])
        )

        start = current_time
        end = start + selected["burst"]

        gantt.append((selected["pid"], start, end))
        current_time = end
        remaining.remove(selected)

    return calculate_metrics(processes, gantt), gantt


def display_results(results, gantt):
    print("\n" + "=" * 85)
    print("                  CPU SCHEDULING RESULTS")
    print("=" * 85)

    print(
        f"{'PID':<8}{'AT':<8}{'BT':<8}"
        f"{'CT':<8}{'TAT':<8}{'WT':<8}{'RT':<8}"
    )

    for r in sorted(results, key=lambda x: x["pid"]):
        print(
            f"{r['pid']:<8}{r['arrival']:<8}{r['burst']:<8}"
            f"{r['completion']:<8}{r['turnaround']:<8}"
            f"{r['waiting']:<8}{r['response']:<8}"
        )

    avg_wt = sum(r["waiting"] for r in results) / len(results)
    avg_tat = sum(r["turnaround"] for r in results) / len(results)
    avg_rt = sum(r["response"] for r in results) / len(results)

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))
    print("Average Response Time:", round(avg_rt, 2))

    print("\nGANTT CHART")
    print("-" * 60)

    for pid, start, end in gantt:
        print(f"| {pid} ({start}-{end}) ", end="")

    print("|")
    print("-" * 60)


def get_processes():
    processes = []

    try:
        n = int(input("\nEnter number of processes: "))

        if n <= 0:
            print("Number of processes must be positive.")
            return None

        for i in range(n):
            print(f"\nProcess P{i + 1}")

            arrival = int(input("Arrival Time: "))
            burst = int(input("Burst Time: "))

            if arrival < 0 or burst <= 0:
                print("Invalid input! Arrival must be >= 0 and Burst > 0.")
                return None

            processes.append({
                "pid": f"P{i + 1}",
                "arrival": arrival,
                "burst": burst,
                "priority": 0
            })

        return processes

    except ValueError:
        print("Invalid input! Please enter integers only.")
        return None


def run_cpu_scheduling():
    while True:
        print("\n========== CPU SCHEDULING ==========")
        print("1. FCFS")
        print("2. SJF (Non-Preemptive)")
        print("3. Round Robin")
        print("4. Priority (Non-Preemptive)")
        print("5. Back to Main Menu")

        choice = input("\nSelect algorithm (1-5): ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Try again.")
            continue

        processes = get_processes()

        if processes is None:
            continue

        if choice == "1":
            results, gantt = fcfs(processes)
            name = "FCFS"

        elif choice == "2":
            results, gantt = sjf(processes)
            name = "SJF Non-Preemptive"

        elif choice == "3":
            try:
                quantum = int(input("Enter Time Quantum: "))

                if quantum <= 0:
                    print("Time Quantum must be positive.")
                    continue

                results, gantt = round_robin(processes, quantum)
                name = "Round Robin"

            except ValueError:
                print("Invalid quantum! Enter an integer.")
                continue

        else:
            try:
                for p in processes:
                    p["priority"] = int(
                        input(f"Enter priority for {p['pid']} (lower = higher): ")
                    )

                results, gantt = priority_scheduling(processes)
                name = "Priority Scheduling"

            except ValueError:
                print("Invalid priority! Enter an integer.")
                continue

        print(f"\nAlgorithm: {name}")
        display_results(results, gantt)


if __name__ == "__main__":
    run_cpu_scheduling()
