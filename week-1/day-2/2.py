Question Name: Maximizing Greatness

def max_greatness(nums):
    sorted_nums = sorted(nums)
    nums = sorted(nums)  # Sort the input array
    perm = []
    j = 0  # Pointer for the sorted array

    for num in nums:
        # Find the smallest element in sorted_nums that is greater than num
        while j < len(sorted_nums) and sorted_nums[j] <= num:
            j += 1
        
        if j < len(sorted_nums):
            perm.append(sorted_nums[j])
            j += 1
        else:
            break

    return len(perm)
n=int(input())
nums=list(map(int,input().split()))
print(max_greatness(nums))
