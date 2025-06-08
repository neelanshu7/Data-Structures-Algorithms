class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Traversal
    def traversal(self):
        if not self.head:
            print("List is empty")
            return
        ptr = self.head
        i = 0
        while True:
            print(f"Element{i} : {ptr.data}")
            ptr = ptr.next
            i += 1
            if ptr == self.head:
                break

    # 2.1 Insert at First
    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # circular link
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = self.head
            self.head = new_node

    # 2.2 Insert at Index
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insert_at_first(data)
            return
        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next
            if ptr == self.head:
                raise IndexError("Index out of range")
        new_node.next = ptr.next
        ptr.next = new_node

    # 2.3 Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = self.head

    # 2.4 Insert After Node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# === Main Code ===
cll = CircularLinkedList()

# Node creation manually (equivalent to head, second, third, fourth)
node1 = Node(20)
node2 = Node(30)
node3 = Node(50)
node4 = Node(60)

# Connecting nodes circularly
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
cll.head = node1

# Traversal before insertion
print("Before Insert")
cll.traversal()

# Insert at first
print("\nInsert at First")
cll.insert_at_first(100)
cll.insert_at_first(110)
cll.insert_at_first(120)
cll.traversal()

# Insert at index
print("\nAfter Insert At Index")
cll.insert_at_index(401, 2)
cll.traversal()

# Insert at end
print("\nAfter Insert At End")
cll.insert_at_end(701)
cll.traversal()

# Insert after specific node
print("\nAfter Insert After Node")
cll.insert_after_node(node3, 801)
cll.traversal()
