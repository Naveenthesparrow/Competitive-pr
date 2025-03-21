Question Name: sum_of_subarray_mins

def sum_of_subarray_mins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    # Arrays to store the previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    
    stack = []
    
    # Find previous smaller for each element
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)
    
    stack = []
    
    # Find next smaller for each element
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            next_smaller[stack[-1]] = i
            stack.pop()
        stack.append(i)
    
    # Calculate the result using the contribution of each element
    result = 0
    for i in range(n):
        result += arr[i] * (i - prev_smaller[i]) * (next_smaller[i] - i)
        result %= MOD
    
    return result

# Function to take input from user
def user_input():
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

    if len(arr) != n:
        print("Input size does not match the number of elements entered.")
        return

    result = sum_of_subarray_mins(arr)
    print("The sum of min(b) for every subarray is:", result)

# Call the function to take input and compute the result
user_input()
