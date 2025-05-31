from typing import List
# use return a[0] <= b[1] and b[0] <= a[1] if endpoints are inclusive
def is_overlap(a, b):
    return a[0] < b[1] and b[0] < a[1]

# Example usage:
interval1 = (1, 5)
interval2 = (4, 8)
overlap = is_overlap(interval1, interval2)
print(f"Do intervals {interval1} and {interval2} overlap? {overlap}")

def get_intersection(a, b):
    # Assumes intervals are [start, end] where start <= end
    # If they don't overlap, return None or an empty interval depending on problem needs.
    if not (a[0] <= b[1] and b[0] <= a[1]): # Using the "touching" overlap check
        return None # Or [] or a default value like (0,0) if range is [0,0]

    return [max(a[0], b[0]), min(a[1], b[1])]

# Example usage:
print(f"Intersection of [1,5] and [4,8]: {get_intersection((1, 5), (4, 8))}") # Expected: [4, 5]
print(f"Intersection of [1,3] and [3,5]: {get_intersection((1, 3), (3, 5))}") # Expected: [3, 3]
print(f"Intersection of [1,2] and [3,4]: {get_intersection((1, 2), (3, 4))}") # Expected: None

def merge_overlapping_intervals(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

# Example usage:
interval1 = (1, 5)
interval2 = (4, 8)
merged_interval = merge_overlapping_intervals(interval1, interval2)
print(f"Merged interval of {interval1} and {interval2}: {merged_interval}")

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by the first element
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if is_overlap(last_merged, current):
            merged[-1] = merge_overlapping_intervals(last_merged, current)
        else:
            merged.append(current)
    
    return merged

# Example usage:
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_intervals(intervals)
print("Merged intervals:", merged_intervals)

def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals that come strictly before the new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge overlapping intervals (including the new_interval)
    while i < n and new_interval[1] >= intervals[i][0]: # Use >= for touching overlap
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval) # Add the merged new_interval

    # 3. Add all remaining intervals that come strictly after the new_interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example usage:
intervals = [[1,3],[6,9]]
new_interval = [2,5]
print(f"Insert {new_interval} into {intervals}: {insert_interval(intervals, new_interval)}") # Expected: [[1,5],[6,9]]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval2 = [4,8]
print(f"Insert {new_interval2} into {intervals2}: {insert_interval(intervals2, new_interval2)}") # Expected: [[1,2],[3,10],[12,16]]

def max_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    Finds the maximum number of overlapping intervals at any single point in time.
    """
    events = []
    for start, end in intervals:
        events.append((start, 1)) # +1 for start of an interval
        events.append((end, -1))  # -1 for end of an interval

    # Sort events: by time, then by type (-1 before +1 for same time to handle overlaps correctly)
    # Sorting by type ensures that an interval ending at X is processed before one starting at X,
    # preventing miscounting if start and end points coincide.
    events.sort(key=lambda x: (x[0], x[1])) 

    max_overlap = 0
    current_overlap = 0

    for time, type_val in events:
        current_overlap += type_val
        max_overlap = max(max_overlap, current_overlap)

    return max_overlap

# Example usage:
meetings = [[0, 30], [5, 10], [15, 20]]
print(f"Max overlapping meetings: {max_overlapping_intervals(meetings)}") # Expected: 2 (at time 5-10 and 15-20)

meetings2 = [[1, 5], [2, 6], [3, 7], [4, 8]]
print(f"Max overlapping meetings: {max_overlapping_intervals(meetings2)}") # Expected: 4 (at time 4-5)

# Example: Sort by end time, then by start time if end times are equal
def custom_sort_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: (x[1], x[0]))
    return intervals

# Example usage:
intervals = [[1, 4], [0, 4], [3, 5], [2, 3]]
sorted_intervals = custom_sort_intervals(intervals)
print(f"Custom sorted intervals: {sorted_intervals}") # Expected: [[2,3], [0,4], [1,4], [3,5]]