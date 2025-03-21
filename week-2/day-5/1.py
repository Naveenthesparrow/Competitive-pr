Question Name: Meeting Rooms II



import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    
    return len(heap)

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2