from typing import List
def sortArray(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums # Base case: a list with 0 or 1 element is already sorted

    mid = len(nums) // 2
    left_half = sortArray(nums[:mid])    # Recursively sort the left half
    right_half = sortArray(nums[mid:])   # Recursively sort the right half

    return merge(left_half, right_half) # Merge the sorted halves

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.
    """
    merged = []
    left_ptr, right_ptr = 0, 0

    # Compare elements from both lists and append the smaller one
    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] <= right[right_ptr]:
            merged.append(left[left_ptr])
            left_ptr += 1
        else:
            merged.append(right[right_ptr])
            right_ptr += 1

    # Append any remaining elements from the left list
    while left_ptr < len(left):
        merged.append(left[left_ptr])
        left_ptr += 1

    # Append any remaining elements from the right list
    while right_ptr < len(right):
        merged.append(right[right_ptr])
        right_ptr += 1

    return merged

from typing import Optional

class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge Sort for Singly Linked List
class Solution:
    def sortList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sorts a singly linked list using Merge Sort (top-down recursive approach).
        """
        # Base case: If the list is empty or has only one node, it's already sorted.
        if not head or not head.next:
            return head

        # 1. Split the list into two halves
        # Use fast and slow pointers to find the middle of the list.
        # 'slow' will be at the middle, 'prev' will be the node before 'slow'
        slow = head
        fast = head
        prev = None # To break the link for the first half

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 'prev' is now the last node of the first half.
        # Break the link to separate the two halves.
        if prev:
            prev.next = None
        
        # 'head' is the start of the first half.
        # 'slow' is the start of the second half.
        
        # 2. Recursively sort the two halves
        left_half = self.sortList(head)
        right_half = self.sortList(slow)

        # 3. Merge the sorted halves
        return self._mergeTwoLists(left_half, right_half)

    def _mergeTwoLists(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        """
        Merges two sorted linked lists into a single sorted linked list.
        Uses a dummy node to simplify list construction.
        """
        dummy = Node(0) # Dummy node to simplify appending to the merged list
        current = dummy # Pointer to the last node in the merged list

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next # Move current pointer forward

        # Append any remaining nodes from either list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return dummy.next # The head of the merged list is after the dummy node

# --- Helper function for testing (not part of the Solution class for LeetCode) ---
def create_linked_list(arr: List[int]) -> Optional[Node]:
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head: Optional[Node]):
    if not head:
        print("Empty list")
        return
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))

# --- Example Usage (for local testing) ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Basic sort
    print("Test Case 1: Basic sort")
    list1 = create_linked_list([4, 2, 1, 3])
    print("Original list:")
    print_linked_list(list1)
    sorted_list1 = sol.sortList(list1)
    print("Sorted list:")
    print_linked_list(sorted_list1) # Expected: 1 -> 2 -> 3 -> 4

    # Test Case 2: Empty list
    print("\nTest Case 2: Empty list")
    list2 = create_linked_list([])
    print("Original list:")
    print_linked_list(list2)
    sorted_list2 = sol.sortList(list2)
    print("Sorted list:")
    print_linked_list(sorted_list2) # Expected: Empty list

    # Test Case 3: Single node list
    print("\nTest Case 3: Single node list")
    list3 = create_linked_list([7])
    print("Original list:")
    print_linked_list(list3)
    sorted_list3 = sol.sortList(list3)
    print("Sorted list:")
    print_linked_list(sorted_list3) # Expected: 7

    # Test Case 4: Already sorted list
    print("\nTest Case 4: Already sorted list")
    list4 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_linked_list(list4)
    sorted_list4 = sol.sortList(list4)
    print("Sorted list:")
    print_linked_list(sorted_list4) # Expected: 1 -> 2 -> 3 -> 4 -> 5

    # Test Case 5: Reverse sorted list
    print("\nTest Case 5: Reverse sorted list")
    list5 = create_linked_list([5, 4, 3, 2, 1])
    print("Original list:")
    print_linked_list(list5)
    sorted_list5 = sol.sortList(list5)
    print("Sorted list:")
    print_linked_list(sorted_list5) # Expected: 1 -> 2 -> 3 -> 4 -> 5

    # Test Case 6: List with duplicates
    print("\nTest Case 6: List with duplicates")
    list6 = create_linked_list([3, 1, 4, 1, 5, 9, 2, 6])
    print("Original list:")
    print_linked_list(list6)
    sorted_list6 = sol.sortList(list6)
    print("Sorted list:")
    print_linked_list(sorted_list6) # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 9