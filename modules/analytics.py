from .disk_scheduling import (
    fcfs_disk,
    sstf_disk,
    scan_disk,
    cscan_disk
)

def run_performance_analysis():
    print("\n========== PERFORMANCE ANALYSIS ==========")

    try:
        disk_size = int(input("Enter total number of disk tracks: "))
        head = int(input("Enter initial head position: "))

        if disk_size <= 0 or head < 0 or head >= disk_size:
            print("Error: Invalid disk size or head position.")
            return

        requests = list(map(int, input(
            "Enter disk requests separated by spaces: "
        ).split()))

        if not requests:
            print("Error: At least one request is required.")
            return

        if any(x < 0 or x >= disk_size for x in requests):
            print("Error: Request outside disk boundaries.")
            return

        print("\nChoose direction:")
        print("1. Right")
        print("2. Left")

        choice = input("Enter choice (1-2): ").strip()

        if choice not in ("1", "2"):
            print("Error: Invalid direction.")
            return

        direction = "right" if choice == "1" else "left"

        results = {}

        results["FCFS"] = fcfs_disk(requests, head)[1]
        results["SSTF"] = sstf_disk(requests, head)[1]
        results["SCAN"] = scan_disk(
            requests, head, disk_size, direction
        )[1]
        results["C-SCAN"] = cscan_disk(
            requests, head, disk_size, direction
        )[1]

        print("\n========== PERFORMANCE COMPARISON ==========")
        print(f"{'Algorithm':<15}{'Head Movement':<20}")
        print("-" * 35)

        for name, movement in results.items():
            print(f"{name:<15}{movement:<20} tracks")

        best_algorithm = min(results, key=results.get)
        best_movement = results[best_algorithm]
        fcfs_movement = results["FCFS"]

        if fcfs_movement > 0:
            improvement = (
                (fcfs_movement - best_movement) / fcfs_movement
            ) * 100
        else:
            improvement = 0

        print("\n========== ANALYSIS SUMMARY ==========")
        print("Best Performing Algorithm:", best_algorithm)
        print("Minimum Head Movement:", best_movement, "tracks")
        print(
            f"Improvement over FCFS: {improvement:.2f}%"
        )

        print("\nAlgorithm Ranking:")

        ranked = sorted(results.items(), key=lambda item: item[1])

        for position, (name, movement) in enumerate(ranked, start=1):
            print(f"{position}. {name} - {movement} tracks")

    except ValueError:
        print("Error: Please enter valid integer values.")


if __name__ == "__main__":
    run_performance_analysis()
