from typing import List
import random # For better pivot selection

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using the QuickSort algorithm.
        This is the main entry point for LeetCode problems.
        """
        self._quicksort(nums, 0, len(nums) - 1)
        return nums

    def _quicksort(self, nums: List[int], low: int, high: int) -> None:
        """
        Recursive helper function for QuickSort.
        Sorts the sub-array nums[low...high].
        """
        if low < high:
            # pi is partitioning index, nums[pi] is now at right place
            pi = self._partition(nums, low, high)

            # Recursively sort elements before partition and after partition
            self._quicksort(nums, low, pi - 1)
            self._quicksort(nums, pi + 1, high)

    def _partition(self, nums: List[int], low: int, high: int) -> int:
        """
        Partitions the sub-array nums[low...high] around a pivot.
        Elements smaller than pivot are moved to the left, larger to the right.
        Returns the final index of the pivot element.
        """
        # Choose a random pivot to mitigate worst-case O(N^2) for sorted/reverse-sorted arrays.
        # A more robust pivot selection might be "median-of-three".
        random_pivot_index = random.randint(low, high)
        nums[random_pivot_index], nums[high] = nums[high], nums[random_pivot_index]
        
        pivot = nums[high] # Choose the last element as pivot (after possibly swapping a random one there)
        
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i] # Swap if element is smaller than pivot

        # Swap the pivot element with the element at i + 1
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        
        return i + 1 # Return the partitioning index


# --- Example Usage (for local testing) ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Basic sort
    print("--- Test Case 1: Basic Sort ---")
    arr1 = [5, 2, 3, 1]
    print(f"Original: {arr1}")
    sol.sortArray(arr1)
    print(f"Sorted:   {arr1}") # Expected: [1, 2, 3, 5]

    # Test Case 2: Duplicates
    print("\n--- Test Case 2: Duplicates ---")
    arr2 = [5, 1, 1, 2, 0, 0]
    print(f"Original: {arr2}")
    sol.sortArray(arr2)
    print(f"Sorted:   {arr2}") # Expected: [0, 0, 1, 1, 2, 5]

    # Test Case 3: Empty list
    print("\n--- Test Case 3: Empty List ---")
    arr3 = []
    print(f"Original: {arr3}")
    sol.sortArray(arr3)
    print(f"Sorted:   {arr3}") # Expected: []

    # Test Case 4: Single element
    print("\n--- Test Case 4: Single Element ---")
    arr4 = [7]
    print(f"Original: {arr4}")
    sol.sortArray(arr4)
    print(f"Sorted:   {arr4}") # Expected: [7]

    # Test Case 5: Already sorted
    print("\n--- Test Case 5: Already Sorted ---")
    arr5 = [1, 2, 3, 4, 5]
    print(f"Original: {arr5}")
    sol.sortArray(arr5)
    print(f"Sorted:   {arr5}") # Expected: [1, 2, 3, 4, 5]

    # Test Case 6: Reverse sorted
    print("\n--- Test Case 6: Reverse Sorted ---")
    arr6 = [5, 4, 3, 2, 1]
    print(f"Original: {arr6}")
    sol.sortArray(arr6)
    print(f"Sorted:   {arr6}") # Expected: [1, 2, 3, 4, 5]

    # Test Case 7: Larger random array
    print("\n--- Test Case 7: Larger Random Array ---")
    arr7 = [random.randint(0, 100) for _ in range(20)]
    print(f"Original: {arr7}")
    sol.sortArray(arr7)
    print(f"Sorted:   {arr7}")
    print(f"Is sorted: {arr7 == sorted(arr7)}") # Verify with Python's built-in sort