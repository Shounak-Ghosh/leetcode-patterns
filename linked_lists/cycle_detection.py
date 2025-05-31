class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_cycle(self):
        """
        Detects if a cycle exists in the linked list using fast and slow pointers.
        Returns True if a cycle is found, False otherwise.
        """
        if not self.head or not self.head.next:
            # A list with 0 or 1 node cannot have a cycle
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next          # Slow pointer moves one step
            fast = fast.next.next     # Fast pointer moves two steps

            if slow == fast:
                # If they meet, a cycle is detected
                return True

        # If fast reaches the end (None) or fast.next is None, no cycle
        return False

    def find_cycle_start(self):
        """
        Detects if a cycle exists and, if so, returns the node where the cycle begins.
        Returns None if no cycle is found.
        """
        if not self.head or not self.head.next:
            return None

        slow = self.head
        fast = self.head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected. Now find the start of the cycle.
                break
        else: # This 'else' belongs to the while loop, executes if loop finishes without a 'break'
            return None # No cycle found

        # Phase 2: Find cycle start
        # Move one pointer to the head, keep the other at the meeting point.
        # Move both one step at a time. They will meet at the cycle start.
        # This can be proved mathematically -- Floyd's Cycle Detection Algorithm.
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow # Both pointers are now at the cycle start node

# --- Example Usage ---

# 1. No Cycle
print("--- Test Case 1: No Cycle ---")
ll_no_cycle = LinkedList()
ll_no_cycle.append(1)
ll_no_cycle.append(2)
ll_no_cycle.append(3)
ll_no_cycle.append(4)
print(f"Cycle detected: {ll_no_cycle.find_cycle()}") # Expected: False
print(f"Cycle start: {ll_no_cycle.find_cycle_start()}") # Expected: None

# 2. Cycle at the head
print("\n--- Test Case 2: Cycle at Head ---")
ll_cycle_head = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1 # Cycle! 3 points back to 1
ll_cycle_head.head = node1
print(f"Cycle detected: {ll_cycle_head.find_cycle()}") # Expected: True
cycle_start_node_head = ll_cycle_head.find_cycle_start()
print(f"Cycle start value: {cycle_start_node_head.value if cycle_start_node_head else None}") # Expected: 1

# 3. Cycle in the middle
print("\n--- Test Case 3: Cycle in the Middle ---")
ll_cycle_middle = LinkedList()
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_c # Cycle! E points back to C

ll_cycle_middle.head = node_a
print(f"Cycle detected: {ll_cycle_middle.find_cycle()}") # Expected: True
cycle_start_node_middle = ll_cycle_middle.find_cycle_start()
print(f"Cycle start value: {cycle_start_node_middle.value if cycle_start_node_middle else None}") # Expected: C

# 4. Single node cycle
print("\n--- Test Case 4: Single Node Cycle ---")
ll_single_node_cycle = LinkedList()
single_node = Node(100)
single_node.next = single_node # Cycle!
ll_single_node_cycle.head = single_node
print(f"Cycle detected: {ll_single_node_cycle.find_cycle()}") # Expected: True
cycle_start_single = ll_single_node_cycle.find_cycle_start()
print(f"Cycle start value: {cycle_start_single.value if cycle_start_single else None}") # Expected: 100

# 5. Two node cycle
print("\n--- Test Case 5: Two Node Cycle ---")
ll_two_node_cycle = LinkedList()
node_x = Node('X')
node_y = Node('Y')
node_x.next = node_y
node_y.next = node_x # Cycle!
ll_two_node_cycle.head = node_x
print(f"Cycle detected: {ll_two_node_cycle.find_cycle()}") # Expected: True
cycle_start_two = ll_two_node_cycle.find_cycle_start()
print(f"Cycle start value: {cycle_start_two.value if cycle_start_two else None}") # Expected: X