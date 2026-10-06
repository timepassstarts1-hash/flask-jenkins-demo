def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move Disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move Disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter the number of disks: "))

print("\nTower of Hanoi Steps:\n")
tower_of_hanoi(n, "A", "B", "C")
