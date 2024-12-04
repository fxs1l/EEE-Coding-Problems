def is_valid_inputs(b, a):
    """Check if the inputs provided are valid"""
    if (b > a > 0) and (b-a) % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    b = int(input("Enter b: "))
    a = int(input("Enter a: "))

    while not is_valid_inputs(b, a):
        print("Invalid input.")
        b = int(input("Enter b: "))
        a = int(input("Enter a: "))

    print()

    spacing = b - 1
    small_triangle = (b - a) / 2
    for i in range(b):
        # do spacing 
        for s in range(spacing):
            print(" ", end ="")
        for j in range(i+i+1):
            if i < small_triangle or i >= small_triangle + a:
                print("*", end = "")
            else:
                if j >= small_triangle and j <= i+i-small_triangle :
                    print("a", end = "")
                else:
                    print("*", end = "")
        print()
        spacing -= 1

