class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        # sentinel head and tail for Node doubly-linked list
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # stores key, Node reference pointers
        self.m = {}

    def addNode(self, newNode):
        temp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = temp
        temp.prev = newNode

    def deleteNode(self, delNode):
        prevv = delNode.prev
        nextt = delNode.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.m:
            # remove from current position
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            # add to front of the list -- most recently used
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        # delete if already exists
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.deleteNode(curr)

        # evict last node (LRU) if capacity reached
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        # create new node and add to front, update map as well
        self.addNode(self.Node(key, value))
        self.m[key] = self.head.next
