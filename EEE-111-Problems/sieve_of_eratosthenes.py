def createList(n):
    #Base Case/s
    #TODO: Add conditions here for your base case/s
    if n == 2 :
        return [2]
    #Recursive Case/s
    #TODO: Add conditions here for your recursive case/s
    else:
        return sorted([n] + createList(n-1))
    #remove the line after this once you've completed all the TODO for this function

def removeMultiples(x, arr):
      #Base Case/s
    #TODO: Add conditions here for your base case/s
    if len(arr) == 1:
        if arr[0] % x != 0:
            return [arr[0]]
        else:
            return []
    #Recursive Case/s
    #TODO: Add conditions here for your recursive case/s
    else:
        if arr[0] % x != 0: # first element is not divisible by x
            return [arr[0]] + removeMultiples(x, arr[1:])
        else:
            return removeMultiples(x, arr[1:])
        #         return [x] + removeMultiples(x+1, arr)
    #remove the line after this once you've completed all the TODO for this function

def Sieve_of_Eratosthenes(list):
    #Base Case/s
    if len(list) == 1:
        return list
    #Recursive Case/s
    else:
        return  [list[0]] + Sieve_of_Eratosthenes(removeMultiples(list[0], list[1:]))

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(n)
    i = 2
    list = createList(n)
    #Solution 1
    primes = Sieve_of_Eratosthenes(list)
    print(primes)
