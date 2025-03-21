Question Name:  Find First and Last Position of Element in Sorted Array


def search_range(nums, target):
    def find_position(left):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo

    left_pos = find_position(True)
    right_pos = find_position(False) - 1

    if left_pos <= right_pos < len(nums) and nums[left_pos] == nums[right_pos] == target:
        return [left_pos, right_pos]
    return [-1, -1]

nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter target value: "))
print("First and last position of target:", search_range(nums, target))

