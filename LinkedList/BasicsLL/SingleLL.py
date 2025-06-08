class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Traversal
def linked_list_traversal(head):
    ptr = head
    i = 0
    while ptr:
        print(f"Element {i}: {ptr.data}")
        ptr = ptr.next
        i += 1

# 2.A Insert at First
def insert_at_first(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# 2.B Insert at Index
def insert_at_index(head, data, index):
    if index == 0:
        return insert_at_first(head, data)
    new_node = Node(data)
    p = head
    i = 0
    while i < index - 1 and p is not None:
        p = p.next
        i += 1
    if p is None:
        print("Index out of bounds")
        return head
    new_node.next = p.next
    p.next = new_node
    return head

# 2.C Insert at End
def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    p = head
    while p.next:
        p = p.next
    p.next = new_node
    return head

# 2.D Insert after Node
def insert_after_node(head, data, prev_node):
    if not prev_node:
        print("Previous node is None")
        return head
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    return head

# 3.1 Delete First
def delete_first(head):
    if not head:
        return None
    return head.next

# 3.2 Delete at Index
def delete_at_index(head, index):
    if index == 0:
        return delete_first(head)
    p = head
    for _ in range(index - 1):
        if p is None or p.next is None:
            print("Index out of bounds")
            return head
        p = p.next
    q = p.next
    if q:
        p.next = q.next
    return head

# 3.3 Delete at End
def delete_end(head):
    if not head or not head.next:
        return None
    p = head
    while p.next.next:
        p = p.next
    p.next = None
    return head

# 3.4 Delete by Value
def delete_by_value(head, value):
    if not head:
        return None
    if head.data == value:
        return head.next
    p = head
    while p.next and p.next.data != value:
        p = p.next
    if p.next and p.next.data == value:
        p.next = p.next.next
    return head

# Main function
def main():
    # Creating the Linked List
    head = Node(20)
    second = Node(30)
    third = Node(50)
    fourth = Node(60)

    head.next = second
    second.next = third
    third.next = fourth

    print("Before Insert")
    linked_list_traversal(head)

    print("Insertion")

    print("After Insert At First")
    head = insert_at_first(head, 11)
    linked_list_traversal(head)

    print("After Insert At Index")
    head = insert_at_index(head, 401, 2)
    linked_list_traversal(head)

    print("After Insert At End")
    head = insert_at_end(head, 701)
    linked_list_traversal(head)

    print("After Insert After Node")
    head = insert_after_node(head, 801, third)
    linked_list_traversal(head)

    print("\nDeletion")

    print("Linked List After Delete First")
    head = delete_first(head)
    linked_list_traversal(head)

    print("Linked List After Delete At Index")
    head = delete_at_index(head, 3)
    linked_list_traversal(head)

    print("Linked List After Delete At End")
    head = delete_end(head)
    linked_list_traversal(head)

    print("Linked List After Delete By Node (Value 69)")
    head = delete_by_value(head, 69)  # Value doesn't exist
    linked_list_traversal(head)

if __name__ == "__main__":
    main()
