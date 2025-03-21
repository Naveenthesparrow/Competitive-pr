Question Name: trapRainWater


def trapRainWater(height):
    if not height:
        return 0
    
    n = len(height)
    
    # Arrays to store the maximum height to the left and right of each bar
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Fill right_max array
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]
    
    return trapped_water

# Function to take input from user
def user_input():
    n = int(input("Enter the number of elements in the height array: "))
    height = list(map(int, input("Enter the elements of the height array separated by space: ").split()))

    if len(height) != n:
        print("Input size does not match the number of elements entered.")
        return

    result = trapRainWater(height)
    print("The total amount of water that can be trapped is:", result)

# Call the function to take input and compute the result
user_input()
