def is_overlap(a, b):
    return a[0] < b[1] and b[0] < a[1]

# Example usage:
interval1 = (1, 5)
interval2 = (4, 8)
overlap = is_overlap(interval1, interval2)
print(f"Do intervals {interval1} and {interval2} overlap? {overlap}")

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
