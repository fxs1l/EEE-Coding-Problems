import sys
sys.setrecursionlimit(10000)
def count_permutations(digits, price, n_factorial):
    digit_len = len(digits)
    old_digits = tuple(digits)
    
    if digit_len == len(set(digits)): # no duplicates
        permutations = n_factorial
    permutations = n_factorial / factorial_duplicates(digits) # if there are digits with duplicates
    # distribute the digits
    for n in range(digit_len-1,0,-1):
        if digits[n-1]-digits[n] > 0 and digits[n-1] != 1:
            space_left = digit_len - n + 1
            price = sum(i for i in digits[n-1:])
            if price - (digits[n-1]-1) * space_left <= 0:
                digits[n-1] -= 1
                raw = get_max_digits(price, digits[n-1])
                digits = digits[0:n-1] + raw + (len(digits)-len(raw)-len(digits[0:n-1]))*[0]
                break

    new_sum = sum(i for i in digits)
    if sorted(digits) == sorted(old_digits):
        return permutations - 1
    else:
        return permutations + count_permutations(digits, price, n_factorial)

def factorial_duplicates(digits):
    duplicates = [i for i in digits if digits.count(i) > 1]
    multiply = 1
    for i in list(set(duplicates)):
        multiply *= factorial(digits.count(i))
    return multiply

def get_max_digits(price, max_d):
    if price <= max_d:
        return [price]
    else:
        return [max_d] + get_max_digits(price-max_d, max_d)
        
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
        
if __name__ == "__main__":
    item = str(input())
    price = sum(int(i,16) for i in item[2:])
    digit_len = len(item[2:])
    max_digits = get_max_digits(price, 15)
    if len(max_digits) < digit_len:
        max_digits = max_digits + (digit_len - len(max_digits))*[0]
    n_factorial = factorial(digit_len) # possible combinations or n!
    print(int(count_permutations(max_digits, price, n_factorial)))

