Question Name:  Container With Most Water


def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = list(map(int, input("Enter heights separated by space: ").split()))
print("Maximum water that can be contained:", max_area(height))
