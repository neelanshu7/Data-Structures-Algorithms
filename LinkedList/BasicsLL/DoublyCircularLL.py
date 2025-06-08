class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Traversal (Forward)
    def traverse_forward(self):
        if not self.head:
            print("List is empty")
            return
        print("Forward Traversal:")
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    # 2. Traversal (Backward)
    def traverse_backward(self):
        if not self.head:
            print("List is empty")
            return
        print("Backward Traversal:")
        tail = self.head.prev
        temp = tail
        while True:
            print(temp.data, end=" ")
            temp = temp.prev
            if temp == tail:
                break
        print()

    # 3. Insert at Beginning
    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node
            self.head = new_node

    # 4. Insert at End
    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_first(data)
        else:
            new_node = Node(data)
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node

    # 5. Insert at Index
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_first(data)
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp == self.head:
                raise IndexError("Index out of range")
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    # 6. Insert after a given node (by value)
    def insert_after_value(self, after_value, data):
        temp = self.head
        while True:
            if temp.data == after_value:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Value not found")

    # 7. Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            if temp.data == value:
                if temp.next == temp:  # only one node
                    self.head = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.head:
                        self.head = temp.next
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Value not found")

    # 8. Delete a node by index
    def delete_at_index(self, index):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if index == 0:
            self.delete_by_value(self.head.data)
            return
        for _ in range(index):
            temp = temp.next
            if temp == self.head:
                raise IndexError("Index out of range")
        self.delete_by_value(temp.data)

    # 9. Search a node by value
    def search(self, value):
        if not self.head:
            return -1
        temp = self.head
        index = 0
        while True:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
            if temp == self.head:
                break
        return -1

# Create the list
dll = DoublyCircularLinkedList()

# Insert elements
dll.insert_at_first(30)
dll.insert_at_first(20)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.insert_at_index(25, 1)
dll.insert_after_value(40, 45)

# Traversals
dll.traverse_forward()
dll.traverse_backward()

# Deletion
dll.delete_by_value(25)
dll.delete_at_index(2)

# Search
print("Index of 45:", dll.search(45))
print("Index of 100:", dll.search(100))  # Not found

dll.traverse_forward()