def print_multiples(a,b,x):
    #Base Case/s
    #TODO: Add conditions here for your base case/s
    if a == b:
        if x % 2 == 0:
            if a % x == 0:
                return str(a)
            else:
                return ""
        else:
            if b % x == 0:
                return str(b)
            else:
                return ""
        
    #Recursive Case/s
    #TODO: Add conditions here for your recursive case/s
    else:
        if x % 2 == 0:   
            if b % x == 0:
                return str(b) + " " + str(print_multiples(a, b-1, x))
            else:
                return str(print_multiples(a, b-1, x))
        else:
            if a % x == 0:
                return str(a) + " " + str(print_multiples(a+1, b, x))
            else:
                return str(print_multiples(a+1, b, x))

a = int(input("Please enter a: "))
print(a)
b = int(input("Please enter b: "))
print(b)
x = int(input("Please enter x: "))
print(x)
      
if a <= b and a-b <= 200:
    print(print_multiples(a,b,x))
