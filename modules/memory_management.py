
# ==========================================
# OS ResourceX - Memory Management Module
# Algorithms: First Fit, Best Fit, Worst Fit
# ==========================================

def first_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i, process in enumerate(processes):
        for j in range(len(memory)):
            if memory[j] >= process:
                allocation[i] = j
                memory[j] -= process
                break

    return allocation, memory


def best_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i, process in enumerate(processes):
        best_index = -1

        for j in range(len(memory)):
            if memory[j] >= process:
                if (best_index == -1 or
                        memory[j] < memory[best_index]):
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            memory[best_index] -= process

    return allocation, memory


def worst_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i, process in enumerate(processes):
        worst_index = -1

        for j in range(len(memory)):
            if memory[j] >= process:
                if (worst_index == -1 or
                        memory[j] > memory[worst_index]):
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            memory[worst_index] -= process

    return allocation, memory


def display_results(name, blocks, processes, allocation, memory):

    print("\n" + "=" * 65)
    print("MEMORY ALLOCATION RESULTS -", name)
    print("=" * 65)

    print(f"{'Process':<12}{'Size':<12}{'Allocated Block':<20}{'Status'}")

    allocated_memory = 0

    for i, process in enumerate(processes):

        if allocation[i] != -1:
            block_number = allocation[i] + 1
            allocated_memory += process
            status = "Allocated"
        else:
            block_number = "-"
            status = "Not Allocated"

        print(
            f"P{i+1:<11}{process:<12}"
            f"{block_number:<20}{status}"
        )

    total_memory = sum(blocks)
    free_memory = sum(memory)
    utilization = (
        allocated_memory / total_memory * 100
        if total_memory > 0 else 0
    )

    print("\nTotal Memory:", total_memory)
    print("Allocated Memory:", allocated_memory)
    print("Free Memory:", free_memory)
    print("Memory Utilization:", round(utilization, 2), "%")

    print("\nRemaining Memory Blocks:", memory)


def get_input():

    try:
        n = int(input("\nEnter number of memory blocks: "))

        if n <= 0:
            print("Number of blocks must be positive.")
            return None, None

        blocks = []

        for i in range(n):
            size = int(input(f"Enter size of Block {i+1}: "))

            if size <= 0:
                print("Block size must be positive.")
                return None, None

            blocks.append(size)

        m = int(input("\nEnter number of processes: "))

        if m <= 0:
            print("Number of processes must be positive.")
            return None, None

        processes = []

        for i in range(m):
            size = int(input(f"Enter size of Process P{i+1}: "))

            if size <= 0:
                print("Process size must be positive.")
                return None, None

            processes.append(size)

        return blocks, processes

    except ValueError:
        print("Invalid input! Please enter integers only.")
        return None, None


def run_memory_management():

    while True:

        print("\n========== MEMORY MANAGEMENT ==========")
        print("1. First Fit")
        print("2. Best Fit")
        print("3. Worst Fit")
        print("4. Compare All Algorithms")
        print("5. Back to Main Menu")

        choice = input("\nSelect algorithm (1-5): ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Try again.")
            continue

        blocks, processes = get_input()

        if blocks is None:
            continue

        algorithms = {
            "1": ("First Fit", first_fit),
            "2": ("Best Fit", best_fit),
            "3": ("Worst Fit", worst_fit)
        }

        if choice == "4":
            selected = list(algorithms.values())
        else:
            selected = [algorithms[choice]]

        for name, algorithm in selected:

            allocation, memory = algorithm(blocks, processes)

            display_results(
                name, blocks, processes, allocation, memory
            )


if __name__ == "__main__":
    run_memory_management()
