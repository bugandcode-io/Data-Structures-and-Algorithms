def hanoi(n, source="A", helper="B", target="C"):
    """
    Print the steps to move n disks from source to target using helper.
    """
    if n <= 0:
        return

    if n == 1:
        print(f"Move disk 1: {source} -> {target}")
        return

    # Move n-1 from source to helper
    hanoi(n - 1, source, target, helper)

    # Move the biggest disk to target
    print(f"Move disk {n}: {source} -> {target}")

    # Move n-1 from helper to target
    hanoi(n - 1, helper, source, target)


if __name__ == "__main__":
    n = 3
    hanoi(n)
