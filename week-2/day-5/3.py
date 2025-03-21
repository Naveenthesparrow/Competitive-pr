Question Name: Non-overlapping Intervals

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    count = 0
    
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    
    return count

# Example usage:
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))  # Output: 1
