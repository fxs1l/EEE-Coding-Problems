def is_valid_inputs(n1, n2):
    """Check if the inputs provided are valid"""
    # TODO: Uncomment the next two lines once you've filled it out
    if (n1 > 0 and n2 > 0) and n1 < n2:
        return True
    return False


def is_divisible(dividend: int, divisor: int):
    """Checks if the dividend is divisible by the divisor"""
    # TODO: Fill out code block here to check for divisibility
    # TODO: Remove the line below once you've completed this function
    if dividend % divisor == 0:
        return True
    return False


if __name__ == "__main__":
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))

    while not is_valid_inputs(n1, n2):
        print("Invalid input.")
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))

    condition_A = 0
    condition_B = 0
    condition_C = 0

    # TODO: Insert main process here to find the correct outputs for conditions A, B, and C
    # Checking for outputs
    for i in range(n1+1, n2):
        # Check for conditions that satisfy condition A
        if is_divisible(i, 7) and is_divisible(i, 3) == False:
            condition_A += 1
        if is_divisible(i, 5):
            condition_B += 1
            if is_divisible(i, 9):
                condition_C += 1
                
        
    print(f"Number of integers that satisfy A from {n1} to {n2}: {condition_A}")
    print(f"Number of integers that satisfy B from {n1} to {n2}: {condition_B}")
    print(f"Number of integers that satisfy C from {n1} to {n2}: {condition_C}")

