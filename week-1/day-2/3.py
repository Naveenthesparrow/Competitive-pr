Question Name : Boats to Save People

def num_rescue_boats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    
    return boats

# Example usage:
# Input handling
input_data = input().strip().split()
n = int(input_data[0])
limit = int(input_data[1])
people = list(map(int, input().strip().split()))

result = num_rescue_boats(people, limit)
print(f"Minimum number of boats: {result}")
