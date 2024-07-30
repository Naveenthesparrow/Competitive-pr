Question Name  : Next Greater Element


def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []
    
    # Traverse nums2 from right to left
    for num in reversed(nums2):
        # Maintain the stack such that the top of the stack is the next greater element
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            next_greater[num] = stack[-1]
        else:
            next_greater[num] = -1
        stack.append(num)
    
    # Build the result for nums1 using the next_greater mapping
    result = [next_greater[num] for num in nums1]
    
    return result

# Read input from the user
nums1_length = int(input("Enter the length of nums1: "))
nums1 = list(map(int, input(f"Enter {nums1_length} elements for nums1: ").split()))

nums2_length = int(input("Enter the length of nums2: "))
nums2 = list(map(int, input(f"Enter {nums2_length} elements for nums2: ").split()))

# Check if nums1 is a subset of nums2
if not set(nums1).issubset(set(nums2)):
    print("Error: nums1 is not a subset of nums2")
else:
    # Find the next greater elements
    result = next_greater_element(nums1, nums2)
    
    # Print the result
    print("The next greater elements are:", result)

