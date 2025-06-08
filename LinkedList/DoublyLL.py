class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Traverse Forward
    def traverse_forward(self):
        print("Forward Traversal:")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # 2. Traverse Backward
    def traverse_backward(self):
        print("Backward Traversal:")
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    # 3. Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # 4. Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # 5. Insert at Index
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                raise IndexError("Index out of range")
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    # 6. Insert after a node by value
    def insert_after_value(self, target, data):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
        print("Target value not found")

    # 7. Delete by Value
    def delete_by_value(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Value not found")

    # 8. Delete by Index
    def delete_at_index(self, index):
        if not self.head:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        for _ in range(index):
            temp = temp.next
            if not temp:
                raise IndexError("Index out of range")
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    # 9. Search
    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1
dll = DoublyLinkedList()

# Insertions
dll.insert_at_beginning(30)
dll.insert_at_beginning(20)
dll.insert_at_end(40)
dll.insert_at_index(25, 1)
dll.insert_after_value(40, 45)

# Traversals
dll.traverse_forward()
dll.traverse_backward()

# Deletions
dll.delete_by_value(25)
dll.delete_at_index(2)

# Search
print("Index of 45:", dll.search(45))
print("Index of 100 (not found):", dll.search(100))

dll.traverse_forward()