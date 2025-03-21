Question Name: kthSmallestFraction


import heapq

def kthSmallestFraction(arr, k):
    # Initialize the min-heap
    min_heap = []
    n = len(arr)
    
    # Populate the heap with initial fractions formed with the first element (1)
    for j in range(1, n):
        heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))
    
    # Extract the k-th smallest fraction
    for _ in range(k):
        frac, i, j = heapq.heappop(min_heap)
        if i + 1 < j:
            heapq.heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
    
    # The k-th smallest fraction
    numerator = arr[i]
    denominator = arr[j]
    
    return numerator, denominator

# Example usage:
n, k = map(int, input().split())  # Reading the size of the array and the value of k
arr = list(map(int, input().split()))  # Reading the array elements
numerator, denominator = kthSmallestFraction(arr, k)
print(numerator, denominator)
