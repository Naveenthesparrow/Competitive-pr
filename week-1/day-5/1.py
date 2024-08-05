Question Name: Maximum Subarray Sum


def max_subarray_sum(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

# Input from user
n = int(input("Enter the number of elements in the array: "))
if n == 0:
    print(0)
else:
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    result = max_subarray_sum(arr)
    print(result)
