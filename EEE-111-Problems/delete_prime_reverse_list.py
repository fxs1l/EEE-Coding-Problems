def delete_prime(my_list):
    list = []
    for i in my_list:
        factors = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors.append(j)
        if len(factors) > 2: # is not a prime number
            list.append(i)
    return list

def reverse_list(my_list):
    reversed = []
    i = len(my_list) - 1
    while i >= 0:
        reversed.append(my_list[i])
        i -=1
    print("Reversed:")
    print(reversed)
    
if __name__ == "__main__":
    S = []
    list_len = int(input())
    for i in range(list_len):
        S.append(int(input()))
    prime_removed = delete_prime(S)
    print("Prime Removed:")
    print(prime_removed)
    reverse_list(S)
    
    
    
    
    
