Question Name: Total Fruits

def total_fruit(fruits):
    # Dictionary to count the number of each type of fruit in the current window
    fruit_count = {}
    max_fruits = 0
    left = 0
    
    for right in range(len(fruits)):
        # Add the current fruit to the dictionary
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        
        # If we have more than 2 types of fruits, contract the window from the left
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        # Update the maximum number of fruits
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits

# Example usage:
# Input handling
n = int(input().strip())
fruits = list(map(int, input().strip()))

result = total_fruit(fruits)
print(result)

