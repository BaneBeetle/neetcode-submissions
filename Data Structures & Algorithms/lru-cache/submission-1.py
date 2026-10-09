class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev



class LRUCache:

    def __init__(self, capacity: int):
        self.L = Node(None, None)
        self.R = Node(None, None)
        self.L.next = self.R
        self.R.prev = self.L

        self.capacity = capacity
        self.cache = {}

    def remove(self, node) -> None:
        # Create temp variables
        temp_prev = node.prev
        temp_next = node.next
        # Re-assignment
        temp_prev.next = temp_next
        temp_next.prev = temp_prev

    def insert(self, node) -> None:
        # Move cache[key] up to most recent
        temp_R_prev = self.R.prev
        temp_R_prev.next = node
        node.prev = temp_R_prev
        node.next = self.R
        self.R.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            # Update its position
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        
        if len(self.cache) + 1 > self.capacity:
            # kick out oldest
            oldest = self.L.next
            self.remove(oldest)
            
            # remove from self.cache
            del self.cache[oldest.key]

            # insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
        else:
            # Just add it
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
