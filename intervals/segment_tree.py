class SegmentTree:
    """
    A Segment Tree implementation for Range Sum Queries and Point Updates.
    """

    def __init__(self, arr):
        """
        Initializes the Segment Tree.
        :param arr: The input array.
        """
        self.arr = arr
        self.n = len(arr)
        # The segment tree array will typically need about 4*N space
        # to accommodate all nodes, including those for a potentially non-power-of-2 N.
        self.tree = [0] * (4 * self.n) 
        self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        """
        Recursively builds the segment tree.
        :param node: Current node index in the tree array.
        :param start: Starting index of the segment this node represents in the original array.
        :param end: Ending index of the segment this node represents in the original array.
        """
        # Base case: Leaf node
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            # Recursive step: Build children and combine their results
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            self._build(left_child, start, mid)       # Build left child
            self._build(right_child, mid + 1, end)    # Build right child

            # Current node's value is the sum of its children's values
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, query_start, query_end):
        """
        Performs a range sum query on the segment tree.
        :param query_start: Starting index of the query range (inclusive).
        :param query_end: Ending index of the query range (inclusive).
        :return: The sum of elements in the specified range.
        """
        return self._query(1, 0, self.n - 1, query_start, query_end)

    def _query(self, node, start, end, query_start, query_end):
        """
        Recursive helper for range sum query.
        :param node: Current node index.
        :param start: Start index of the segment this node covers.
        :param end: End index of the segment this node covers.
        :param query_start: Start index of the user's query range.
        :param query_end: End index of the user's query range.
        """
        # Case 1: Current segment is completely outside the query range
        if query_end < start or end < query_start:
            return 0  # Identity for sum query (adding 0 doesn't change sum)

        # Case 2: Current segment is completely inside the query range
        if query_start <= start and end <= query_end:
            return self.tree[node]

        # Case 3: Current segment partially overlaps with the query range
        # Recursively query children and sum their results
        mid = (start + end) // 2
        left_sum = self._query(2 * node, start, mid, query_start, query_end)
        right_sum = self._query(2 * node + 1, mid + 1, end, query_start, query_end)

        return left_sum + right_sum

    def update(self, idx, val):
        """
        Updates the value of an element in the original array and propagates
        the change up the segment tree.
        :param idx: The index of the element to update.
        :param val: The new value for the element.
        """
        # Update the original array first (good practice)
        self.arr[idx] = val
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        """
        Recursive helper for point update.
        :param node: Current node index.
        :param start: Start index of the segment this node covers.
        :param end: End index of the segment this node covers.
        :param idx: The index of the element being updated.
        :param val: The new value for the element at 'idx'.
        """
        # Base case: Leaf node. Update the value at this node.
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        # Determine which child contains the index to be updated
        if start <= idx <= mid:
            self._update(left_child, start, mid, idx, val)
        else:
            self._update(right_child, mid + 1, end, idx, val)

        # After updating the child, update the current node's value
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

# --- Example Usage ---
if __name__ == "__main__":
    # Our example array: [1, 3, 2, 5]
    data = [1, 3, 2, 5]
    print(f"Original array: {data}")

    # Initialize the Segment Tree
    st = SegmentTree(data)
    print(f"Segment Tree array (first {len(st.tree)//4 * 2} elements showing non-zeros):\n{st.tree[:len(st.tree)//4 * 2]}")
    # Visual representation from notes:
    #                     [0,3] Sum=11   (tree[1])
    #                     /      \
    #               [0,1] Sum=4    [2,3] Sum=7  (tree[2], tree[3])
    #               /   \          /   \
    #          [0,0] S=1 [1,1] S=3 [2,2] S=2 [3,3] S=5 (tree[4], tree[5], tree[6], tree[7])

    print("\n--- Query Operations ---")
    # Query for sum in range [0, 3] (entire array)
    q1_start, q1_end = 0, 3
    print(f"Query sum from index {q1_start} to {q1_end}: {st.query(q1_start, q1_end)}") # Expected: 1 + 3 + 2 + 5 = 11

    # Query for sum in range [1, 2] (3 + 2)
    q2_start, q2_end = 1, 2
    print(f"Query sum from index {q2_start} to {q2_end}: {st.query(q2_start, q2_end)}") # Expected: 3 + 2 = 5

    # Query for sum in range [0, 1] (1 + 3)
    q3_start, q3_end = 0, 1
    print(f"Query sum from index {q3_start} to {q3_end}: {st.query(q3_start, q3_end)}") # Expected: 1 + 3 = 4

    # Query for sum in range [3, 3] (just 5)
    q4_start, q4_end = 3, 3
    print(f"Query sum from index {q4_start} to {q4_end}: {st.query(q4_start, q4_end)}") # Expected: 5

    print("\n--- Update Operation ---")
    # Update arr[1] from 3 to 10
    update_idx = 1
    new_value = 10
    print(f"Updating array[{update_idx}] from {st.arr[update_idx]} to {new_value}")
    st.update(update_idx, new_value)
    print(f"Array after update: {st.arr}")
    print(f"Segment Tree array after update (first {len(st.tree)//4 * 2} elements showing non-zeros):\n{st.tree[:len(st.tree)//4 * 2]}")

    print("\n--- Query after Update ---")
    # Query sum in range [0, 3] (entire array)
    # New expected sum: 1 + 10 + 2 + 5 = 18
    q5_start, q5_end = 0, 3
    print(f"Query sum from index {q5_start} to {q5_end}: {st.query(q5_start, q5_end)}") # Expected: 18

    # Query sum in range [1, 2] (10 + 2)
    q6_start, q6_end = 1, 2
    print(f"Query sum from index {q6_start} to {q6_end}: {st.query(q6_start, q6_end)}") # Expected: 10 + 2 = 12