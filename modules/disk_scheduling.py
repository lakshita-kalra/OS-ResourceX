
def fcfs_disk(requests, head):
    order = requests.copy()
    movement = 0
    current = head

    for track in order:
        movement += abs(current - track)
        current = track

    return order, movement


def sstf_disk(requests, head):
    pending = requests.copy()
    order = []
    movement = 0
    current = head

    while pending:
        closest = min(pending, key=lambda x: abs(x - current))
        movement += abs(current - closest)
        current = closest
        order.append(closest)
        pending.remove(closest)

    return order, movement


def scan_disk(requests, head, disk_size, direction):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    order = []
    movement = 0
    current = head

    if direction == "right":
        sequence = right + [disk_size - 1] + left[::-1]

        for track in sequence:
            movement += abs(current - track)
            current = track
            if track != disk_size - 1 or track in requests:
                order.append(track)

    else:
        sequence = left[::-1] + [0] + right

        for track in sequence:
            movement += abs(current - track)
            current = track
            if track != 0 or track in requests:
                order.append(track)

    return order, movement


def cscan_disk(requests, head, disk_size, direction):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    order = []
    movement = 0
    current = head

    if direction == "right":
        sequence = right + [disk_size - 1, 0] + left

    else:
        sequence = left[::-1] + [0, disk_size - 1] + right[::-1]

    for track in sequence:
        movement += abs(current - track)
        current = track

        if track in requests and track not in order:
            order.append(track)

    return order, movement


def display_result(name, order, movement):
    print(f"\n{name}")
    print("Service Order:", " -> ".join(map(str, order)))
    print("Total Head Movement:", movement, "tracks")


def run_disk_scheduling():
    print("\n========== DISK SCHEDULING SIMULATOR ==========")

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
            print("Error: Request must be within disk boundaries.")
            return

        print("\nChoose direction:")
        print("1. Right")
        print("2. Left")

        direction_choice = input("Enter choice (1-2): ")

        if direction_choice not in ("1", "2"):
            print("Error: Invalid direction.")
            return

        direction = "right" if direction_choice == "1" else "left"

        print("\n========== DISK SCHEDULING RESULTS ==========")

        order, movement = fcfs_disk(requests, head)
        display_result("FCFS", order, movement)

        order, movement = sstf_disk(requests, head)
        display_result("SSTF", order, movement)

        order, movement = scan_disk(
            requests, head, disk_size, direction
        )
        display_result("SCAN", order, movement)

        order, movement = cscan_disk(
            requests, head, disk_size, direction
        )
        display_result("C-SCAN", order, movement)

    except ValueError:
        print("Error: Please enter valid integer values.")


if __name__ == "__main__":
    run_disk_scheduling()
