Question Name: Friend Requests I

def num_friend_requests(ages):
    from collections import Counter
    
    ages.sort()
    count = Counter(ages)
    total_requests = 0

    for age in count:
        if age <= 14:
            continue
        valid_min_age = 0.5 * age + 7
        # Calculate how many people are in the valid age range
        # since ages is sorted, we can use binary search to find valid age ranges efficiently
        valid_count = sum(v for k, v in count.items() if k > valid_min_age and k <= age)
        total_requests += valid_count * count[age] - count[age]

    return total_requests

# Example usage
n = int(input().strip())
ages = list(map(int, input().strip().split()))
print(num_friend_requests(ages))
