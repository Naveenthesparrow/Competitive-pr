Question Name:  numRescueBoats


def numRescueBoats(people, limit):
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
n, limit = map(int, input().split())  # Reading the size of the array and the weight limit
people = list(map(int, input().split()))  # Reading the array elements (people's weights)
print(numRescueBoats(people, limit))
