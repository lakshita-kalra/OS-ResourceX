
def calculate_need(maximum, allocation):
    need = []

    for i in range(len(maximum)):
        row = []
        for j in range(len(maximum[i])):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    return need


def banker_safety(allocation, maximum, available):
    process_count = len(allocation)
    resource_count = len(available)

    need = calculate_need(maximum, allocation)

    work = available.copy()
    finish = [False] * process_count
    safe_sequence = []

    while len(safe_sequence) < process_count:
        found = False

        for i in range(process_count):
            if not finish[i]:
                possible = True

                for j in range(resource_count):
                    if need[i][j] > work[j]:
                        possible = False
                        break

                if possible:
                    for j in range(resource_count):
                        work[j] += allocation[i][j]

                    finish[i] = True
                    safe_sequence.append(f"P{i + 1}")
                    found = True

        if not found:
            break

    print("\n========== BANKER'S ALGORITHM ==========")

    print("\nNeed Matrix:")
    for i, row in enumerate(need):
        print(f"P{i + 1}: {row}")

    if all(finish):
        print("\nSystem Status: SAFE STATE")
        print("Safe Sequence:", " -> ".join(safe_sequence))
        print("Deadlock Risk: No deadlock detected.")
    else:
        unfinished = [
            f"P{i + 1}" for i in range(process_count) if not finish[i]
        ]
        print("\nSystem Status: UNSAFE STATE")
        print("Processes unable to complete:", unfinished)
        print("Deadlock Risk: System may enter deadlock.")


def run_deadlock():
    print("\n========== DEADLOCK DETECTION AND AVOIDANCE ==========")

    try:
        process_count = int(input("Enter number of processes: "))
        resource_count = int(input("Enter number of resource types: "))

        if process_count <= 0 or resource_count <= 0:
            print("Error: Counts must be positive.")
            return

        allocation = []
        maximum = []

        print("\nEnter Allocation Matrix:")
        for i in range(process_count):
            row = list(map(int, input(
                f"Allocation for P{i + 1}: "
            ).split()))

            if len(row) != resource_count or any(x < 0 for x in row):
                print("Error: Invalid allocation row.")
                return

            allocation.append(row)

        print("\nEnter Maximum Demand Matrix:")
        for i in range(process_count):
            row = list(map(int, input(
                f"Maximum demand for P{i + 1}: "
            ).split()))

            if len(row) != resource_count or any(x < 0 for x in row):
                print("Error: Invalid maximum demand row.")
                return

            for j in range(resource_count):
                if row[j] < allocation[i][j]:
                    print("Error: Maximum demand cannot be less than allocation.")
                    return

            maximum.append(row)

        available = list(map(int, input(
            "\nEnter available resources: "
        ).split()))

        if len(available) != resource_count or any(x < 0 for x in available):
            print("Error: Invalid available resources.")
            return

        banker_safety(allocation, maximum, available)

    except ValueError:
        print("Error: Please enter valid integer values.")


if __name__ == "__main__":
    run_deadlock()
