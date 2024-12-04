def is_valid_input(x):
    """Check if the input provided is valid"""
    if x <= 0:
         return False
    return True

if __name__ == "__main__":
    x = int(input("Enter num: "))

    while not is_valid_input(x):
        print("Invalid input")
        x = int(input("Enter num: "))
    print()

    spacing = x - 1
    for i in range(x): # height of the triangle
        # do spacing 
        for k in range(spacing):
            print(" ", end ="")
    
        if i > 0:
            for j in range(i+i+1): # width of the triangle
                row = ''
                if j <= 9:
                    print(j, end = "")
                else:
                    print(j%10, end = "")
        
            print()
        else:
            print(i)
        spacing -= 1

