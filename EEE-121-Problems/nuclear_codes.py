import math
size = int(input())
sums = []
grid = []

for i in range(size): # O(n^2)
    row = input().split()
    for r in row:
        grid += [r]
    sums.append(sum(int(j) for j in row))
neg_sums = [i*-1 for i in sums]


# taken from this week's module    
def max_sub_array_r(arr, low, high):
    if high-low > 1:       # if more than one element
        
        mid = (high+low)//2  # find middle
        c1 = max_sub_array_r(arr, low, mid) # operate on left sub-array
        c2 = max_sub_array_r(arr, mid, high)   # operate on right sub-array
        c3 = max_sub_array_cross(arr, low, mid, high) # operate on crossing

        # Note that c1, c2, c3 are 3-element tuples
        # [0] := maximum sum 
        # [1] := start of max sub-array
        # [2] := end of max sub-array

        cmax = c1 if c1[0] > c2[0] else c2
        cmax = c3 if c3[0] > cmax[0] else cmax
        return cmax
    elif high-low == 1:   
        return (arr[low], low, high)  # return single element value
    else:
        return ((-1000*2000), low, high) # return large negative value

def max_sub_array_cross(arr, start, mid, end):

    # Getting maximum sub-array ending at mid
    max_sum_left = (-1000*2000) +1 # some large negative number
    left = -1     # initial border of left max sub-array
    sum_left = 0  # initial sum
    i = mid-1     # start loop at mid-1
    count = 0     # odd-even
    while i >= start:
        if count % 2 != 0:
            sum_left += arr[i]
        else:
            sum_left -= arr[i]
        
        if sum_left > max_sum_left: # new max sub-array found
            max_sum_left = sum_left   # update values
            left = i
        i -= 1      # decrement since we're moving to the left
        count += 1

    # Getting maximum sub-array starting at mid
    max_sum_right = (-1000*2000)+1 # some large negative number
    right = -1    # initial border of right max sub-array
    sum_right = 0 # initial sum
    i = mid       # start loop at mid + 1
    count = 0     # odd-even 
    while i < end:
        if count % 2 == 0:
            sum_right += arr[i]
        else:
            sum_right -= arr[i]
        if sum_right > max_sum_right: # new max sub-array found
            max_sum_right = sum_right   # update values
            right = i
        i += 1      # decrement since we're moving to the left
        count += 1

    return(abs(max_sum_left+max_sum_right), left, right)
def max_sub_array(arr):
    return max_sub_array_r(arr, 0, len(arr))

if size == 1:
    print(grid[0])

else:
    sum1, l1, r1 = max_sub_array(sums)
    sum2, l2, r2 = max_sub_array(neg_sums)
    l, r = l1, r1
    if sum1 < sum2:
        l, r = l2, r2
    if l==r:
        print(math.sqrt(-1))
    for i in range(l, r+1):
        grid_idx = (size*i) + (i-l)
        print(grid[grid_idx])
    
    
